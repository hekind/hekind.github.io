---
layout: post
title:  Attention机制简介
date:   2019-5-30 15:00:00 +0800
categories: document
tag: Deep Learning
---


## Introduction

Attention机制在自然语言处理、图像识别等深度学习领域都取得了一定的进展，包括前段时间Google的Attention is All your need，这一切都说明Attention成为了研究的热点。

Attention机制主要是利用了人在看图像或者阅读文字的时候注意力的分配机制，当人们在阅读或者看某个东西的时候往往是有意识地去注意某些地方，不会去每个细节地进行仔细观察。如下图，图中颜色越深就代表注意力花费更多的地方，我们可以看到注意力集中在婴儿的头部、文章的标题和开始的几句。

<dev align=center>
![attention](https://pic4.zhimg.com/80/v2-2e36652c48659a36f7fe766b2d3056a3_hd.jpg)

[https://zhuanlan.zhihu.com/p/37601161](https://pic4.zhimg.com/80/v2-2e36652c48659a36f7fe766b2d3056a3_hd.jpg)
</dev>

Attention的本质就是一组参数，而这组参数就可以让网络更加关注某些特定的区域，忽略其他的无用的区域，attention机制的目的就是为了学习这组参数。


## Encoder-Decoder模型

Attention机制应用最广泛的是在Seq2Seq模型中，所以我们从Encoder-Encoder谈起。


## Query-Value模型


## 软寻址模型


## Reference

1. [深度学习的注意力机制(2017版) - 张俊林.](https://blog.csdn.net/malefactor/article/details/78767781)
2. [Translation with a Sequence to Sequence Network and Attention - Sean Robertson.](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html#sphx-glr-intermediate-seq2seq-translation-tutorial-py)
3. [浅谈Attention机制的理解 - 知无我.](https://zhuanlan.zhihu.com/p/35571412)
4. [Attention模型方法综述 - PhilippZheng.](https://zhuanlan.zhihu.com/p/37835894)
5. [自然语言处理中的Attention机制总结 - 哈哈进步.](https://blog.csdn.net/hahajinbu/article/details/81940355)


{:toc}