import torch
import torch.nn as nn
import math
class PositionalEncoding(nn.Module):
    """
    位置编码
    """
    def forward(self,x):
        pass
class MultiHeadAttention(nn.Module):
    """
    多头注意力模块
    """
    def forward(self,query,key,value,mask):
        pass
class PositionWiseFeedForward(nn.Module):
    """
    前馈神经网络
    """
    def forward(self,x):
        pass
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
    