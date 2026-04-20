import torch
import torch.nn as nn
import math
class PositionalEncoding(nn.Module):
    """
    位置编码
    """
    def __init__(self,d_model: int,dropout :float =0.1 ,max_len: int =5000):
        super().__init__()
        self.dropout = nn.Dropout(p = dropout)

        #创建足够长的位置编码矩阵
        position = torch.arange(max_len).unsqueeze(1)#增加一维，且此维数的形状大小为1，利于之后广播计算

        div_term = torch.exp(torch.arange(0,d_model,2)*(-math.log(10000.0)/d_model))

        #pe(positional encoding)大小为(max_len,d_model)
        pe = torch.zeros(max_len,d_model)

        #偶数用sin，奇数用cos
        pe[:,0::2] = torch.sin(position*div_term)
        pe[:,1::2] = torch.cos(position*div_term)

        #将pe注册为buffer，这样就不会被视为模型参数，但会随着模型移动(todevice)
        self.register_buffer('pe',pe.unsqueeze(0))
    def forward(self,x: torch.Tensor) ->torch.Tensor :
        # x.size(1)是当前输入sequence的长度
        #将位置编码加到输入向量上
        x = x +self.pe[:,:x.size(1)]
        return self.dropout(x)
        
class MultiHeadAttention(nn.Module):
    """
    多头注意力模块
    """
    def __init__(self,d_model,num_heads):#d_model is the dimension of a token
        super(MultiHeadAttention,self).__init__()
        assert d_model % num_heads ==0

        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model//num_heads

        self.W_q = nn.Linear(d_model,d_model)
        self.W_k = nn.Linear(d_model,d_model)
        self.W_v = nn.Linear(d_model,d_model)#转换的张量，线性变换，可学习
        self.W_o = nn.Linear(d_model,d_model)#将最终多头输出结合的张量，可学习使得其获得更好的结合
    def scaled_dot_product_attention(self,Q,V,K,mask = None):
        #1. 计算注意力得分QK^T
        attn_scores = torch.matmul(Q,K.transpose(-2,-1)/math.sqrt(self.d_k))#transpose方法转换张量维度
        #2.应用掩码（如果提供)
        if mask is not None:
            attn_scores = attn_scores.masked_fill(mask==0,-1e9)#mask==0生成bool型张量，对对应值替换

        #3. 计算注意力权重（softmax）
        attn_probs = torch.softmax(attn_scores,dim=-1)#对-1维度，也就是第j个词元的查询对句子中所有词元的注意力原始分数作softmax

        #4. 加权求和（权重*V)
        output = torch.matmul(attn_probs,V)
        return output
    
    def split_heads(self,x):
        # 将输入 x 的形状从 (batch_size, seq_length, d_model)
        # 变换为 (batch_size, num_heads, seq_length, d_k)
        batch_size,seq_length,d_model = x.size()
        return x.view(batch_size,seq_length,self.num_heads,self.d_k).transpose(1,2)
    
    def combine_heads(self,x):
        batch_size,num_heads,seq_length,d_k = x.size()
        return x.transpose(1,2).continguous().view(batch_size,seq_length,num_heads,d_k)
        #.view(),可以多个维度合并为一个：使用view.(前导维度，-1)即可
        #可以拆分view(前导维度，新维度1，新维度2，新维度3...)
        #要求：内存连续且乘积一致
        #.contiguous方法保证内存的连续性
    def forward(self,query,key,value,mask):
        #1.对QKV线性变换
        Q = self.split_heads(self.W_q(Q))#直接执行矩阵乘法
        K = self.split_heads(self.W_k(K))
        V = self.split_heads(self.W_v(V))
        #2. 计算注意力
        attn_output = self.scaled_dot_product_attention(Q,K,V,mask)

        #3. 合并多头输出并且线性变换
        output = self.W_o(self.combien_heads(attn_output))
        return output
class PositionWiseFeedForward(nn.Module):
    """
    前馈神经网络
    """
    def __init__(self,d_model,d_ff,dropout=0.1):
        super(PositionalEncoding,self).__init__()
        self.linear1 = nn.linear(d_model,d_ff)
        self.droptout = nn.Dropout(dropout)
        self.linear2 = nn.Linear(d_ff,d_model)
        self.relu = nn.ReLU

    def forward(self,x):
        #x形状：(batch_size,seq_len,d_model)
        x = self.linear1(x)
        x = self.Relu(x)
        x = self.dropouy(x)
        x = self.linear2(x)
        #输出形状(batch_size,seq_len,d_model)
        return x
        
#编码器核心层
class EncoderLayer(nn.Module):#继承父类nn.Module
    def __init__(self,d_model,num_heads,d_ff,dropout):
        super(EncoderLayer,self).__init__()
        self.self_attn = MultiHeadAttention()
        self.feed_forward = PositionWiseFeedForward()
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.droptout = nn.Dropout(dropout)
    def forwaed(self,x,mask):
        #残差连接和层归一化
        #1.多头自注意力
        attn_output = self.self_attn(x,x,x,mask)
        x =self.norm1(x+self.droptout(attn_output))

        #2.前馈网络
        ff_output = self.feed_forward(x)
        x = self.nrom2(x+self.droptout(ff_output))

        return x
#解码器核心层
class DecoderLayer(nn.Module):
    def __init__(self,d_model,num_heads,d_ff,dropout):
        super(DecoderLayer,self).__init__()
        self.self_attn = MultiHeadAttention()
        self.cross_attn = MultiHeadAttention()
        self.feed_forward = PositionWiseFeedForward()
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(self.dropout)
    def forward(self,x,encoder_output,src_mask,tgt_mask):
        #1. 掩码多有注意力（自己）
        attn_output = self.self_attn(x,x,x,tgt_mask)
        x = self.norm1(x+self.dropout(attn_output))

        #2. 交叉注意力（对编码器输出）
        cross_attn_output = self.cross_attn(x,encoder_output,encoder_output,src_mask)
        x = self.nrom2(x+self.dropout(cross_attn_output))

        #3. 前馈网络
        ff_output = self.feed_forward(x)
        x = self.norm3(x+self.dropout(ff_output))

        return x
    