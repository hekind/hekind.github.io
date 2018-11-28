---
layout: post
title:  "手动构建比特币交易"
date:   2018-04-06
categories: Translation
tags: Bitcoin
---

> 原文转自腾讯云社区[https://cloud.tencent.com/developer/article/1058930](https://cloud.tencent.com/developer/article/1058930 "原文")，**版权所有，如需转载，请联系翻译作者**

## 介绍

Andreas Antonopoulos曾经提到过，如果他将入狱，他将通过玩数独来重塑比特币共识算法的离线版本。在比特币聚会上进行这样的角色扮演比起最初想象的更有意义，让我解释一下为什么。

在安迪·亨特的[“实用主义思考与学习”](https://pragprog.com/book/ahptl/pragmatic-thinking-and-learning)一书中，他讲述了他如何学习攀岩的故事。首先他花了很多钱去上一堂课，然后教练告诉组员去练习攀岩，而自己去喝咖啡了。便嫌弃教练边爬，过了半个小时后，教练开始解释如何爬墙。经过自己练习获得一些经验后，教练的讲解变得更有容易理解，而不是讲了之后再练习。原因是有**两种主要的学习方式：综合和分析。**如果你无法判断哪一种对应了攀岩课上的练习和讲授，说明你花费的注意力不够。

角色扮演也是一种类似的综合学习体验。由于玩数独游戏需要的你一个人在屏幕前，所以我不会掉进角色扮演的无底洞，而是会用类似的感觉。我们将手把手地去构建一个比特币交易，不会涉及很深入的东西。跟着我走，你就会神奇的理解为什么你的钱包软件给你很多无用的信息。当然，这对于让你赢得[/ r /比特币](https://www.reddit.com/r/Bitcoin/)论证来说非常重要。而且，在一天结束时，它不仅仅是全部？当你在比特币开发和思考过程中困惑的地方，对于那些你无意识中学习深入地地方，它也会为你提供一个全面的理解。

## 要完成本教程，您需要...

...对比特币感兴趣。这就是全部了，你不需要太多编程，你只需要保持**好奇心。**

## 建议

不要害怕这篇文章的长度，你会发现阅读的时候出奇的快，所以继续阅读，它很有趣！

## 步骤

1. 首先生成比特币私钥。
2. 接下来里面存入比特币。
3. 建立交易。
4. 最后提交给网络。

### 视频教程

我记录了[mytest](https://www.youtube.com/watch?v=9ZvMZyVLtqw&feature=youtu.be)，这篇文章是在比特币主网快速完成实验的步骤。

## 演示

### 1.生成您的比特币私钥

![生成所有的东西](https://ask.qcloudimg.com/http-save/1162838/5x60e9r3rs.jpeg)

首先，你需要决定在哪里实验，mainnet(主网)和testnet(测试网络)。选择mainnet意味着你在一个真实的环境中练习；不像是testnet，在测试网络中，比特币没有太多价值，因为可以容易免费地得到。 据尼古拉斯多利尔，C＃的NBitcoin 库的创始人[在mainnet上练习比特币编程](https://programmingblockchain.gitbooks.io/programmingblockchain/content/bitcoin_transfer/bitcoin_address.html)[使错误难以遗忘。](https://programmingblockchain.gitbooks.io/programmingblockchain/content/bitcoin_transfer/bitcoin_address.html)但是它也有其他优点：你可以给我发送你的比特币，作为这篇文章的答谢。

现在请访问[https://www.bitaddress.org/](https://www.bitaddress.org/)(mainnet)或[https://www.bitaddress.org/?testnet=true](https://www.bitaddress.org/?testnet=true)(testnet)，具体取决于您要使用的网络，并为自己生成一对编码:`address（地址，对应了银行卡号）`和`private key(私钥，对应了银行卡密码)`，并记下它。

mainnet比特币地址：`1JdtiE7aN6PekZHXihSJQcSDT2ZGbKNHVe`

testnet比特币地址：`mzXrxNNYrVJgwNL8PGZWTJYbktrhg14kQb`

mainnet私钥：`L3xU6CiTYtL8eBJBscMG8GPsZ2c7NNcX8BYrih4WGmoztLfXByL7`

testnet私钥：`cTLUtfv2Sq5K1yjs5fcRmxitL51i35WmVxaCGUCbfCp722V5aMVY`

### 2.获取一些比特币

接下来给你的比特币地址上存一些比特币。如果你使用的testnet, 谷歌搜索“获得testnet比特币”，你会发现许多网站愿意免费给你提供，比如[这个](http://tpfaucet.appspot.com/)(作者的我打不开，附上自己找的一个网址[https://testnet.manu.backend.hamburg/faucet](https://testnet.manu.backend.hamburg/faucet))。在[区块资源管理器](https://www.smartbit.com.au/)查看您的地址。以下是testnet的区块资源管理器：[https://testnet.smartbit.com.au/adress](https://testnet.smartbit.com.au/)

看看地址：

然后找到你的交易，你要给你的地址发送的东西。[这是我的。](https://testnet.smartbit.com.au/tx/6a04eb2bb7962c03a88332b5a6fe702bd196c4ed366aac634f316694b3150444)  记下交易id：`22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c`

现在我们已经准备好了环境，终于可以开始手动构建我们的交易。

### 3.构建一个交易

现在你有3行信息，保存在一个安全的.txt文件中：

```
Private key(私钥): cTLUtfv2Sq5K1yjs5fcRmxitL51i35WmVxaCGUCbfCp722V5aMVY
Address(地址): mzXrxNNYrVJgwNL8PGZWTJYbktrhg14kQb
Transaction id(交易id): 22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c
```

#### a）检查我们的资金交易

首先让我们看看我们的交易。我们将为此使用[QBit Ninja.](http://docs.qbitninja.apiary.io/) [http://](http://tapi.qbit.ninja/transactions/22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c)[transactions/](http://tapi.qbit.ninja/transactions/22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c)[tapi.qbit.ninja22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c](http://tapi.qbit.ninja/transactions/22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c)

 如果你使用的mainnet ，使用`api.qbit.ninja`

testnet ，则使用`tapi.qbit.ninja`

输出：

```
{
  "transaction": "0100000002d9dced2b6fc80c706d3564670cb6706afe7a798863a9218efcdcf415d58f0f82000000006a473044022030b8bea478444bd52f08de33b082cde1176d3137111f506eefefa91b47b1f6bf02204f12746abd1aeac5805872d163592cf145967fa0619339a9c5348d674852ef4801210224ec1e4c270ce373e6999eebfa01d0a7e7db3c537c026f265233350d5aab81fbfeffffffa0706db65c5e3594d43df5a2a8b6dfd3c9ee506b678f8c26f7820b324b26aa0f000000006a473044022061b718034f876590d6d80bac77a63248b2548d934849acd02c4f4236309e853002201aded6b24f553b6902cf571276b37b12f76b75650164d8738c74469b4edd547e012103d649294a0ca4db920a69eacd6a75cb8a38ae1b81129900621ce45e6ba3438a7bfeffffff0280a90300000000001976a914d0965947ebb329b776328624ebde8f8b32dc639788ac1cc80f00000000001976a914c2a420d34fc86cff932b8c3191549a0ddfd2b0d088acba770f00",
  "transactionId": "22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c",
  "isCoinbase": false,
  "block": null,
  "spentCoins": [
    {
      "transactionId": "820f8fd515f4dcfc8e21a96388797afe6a70b60c6764356d700cc86f2beddcd9",
      "index": 0,
      "value": 100000,
      "scriptPubKey": "76a914e7c1345fc8f87c68170b3aa798a956c2fe6a9eff88ac",
      "redeemScript": null
    },
    {
      "transactionId": "0faa264b320b82f7268c8f676b50eec9d3dfb6a8a2f53dd494355e5cb66d70a0",
      "index": 0,
      "value": 1180443,
      "scriptPubKey": "76a914f3821cff5a90328271d8596198f68e97fbe2ea0e88ac",
      "redeemScript": null
    }
  ],
  "receivedCoins": [
    {
      "transactionId": "22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c",
      "index": 0,
      "value": 240000,
      "scriptPubKey": "76a914d0965947ebb329b776328624ebde8f8b32dc639788ac",
      "redeemScript": null
    },
    {
      "transactionId": "22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c",
      "index": 1,
      "value": 1034268,
      "scriptPubKey": "76a914c2a420d34fc86cff932b8c3191549a0ddfd2b0d088ac",
      "redeemScript": null
    }
  ],
  "firstSeen": "2016-10-31T09:13:18.4420023+00:00",
  "fees": 6175
}
```

是不是很简洁？你需要话多长时间理解那段输出。正如我在开始时所说的，本教程旨在一种综合的学习体验，而不是分析性的学习体验，所以**不要纠结于细节**。如果花费了好几分钟时间，你做错了，下一次尽量快一些。

在本指南，我会向你推荐一些工具以查看更多的信息。这也符合我的目标，为你提供综合学习体验，并希望当你做到\*\*广播你的交易\*\*，您很可能觉得自己学到了一些东西，尽管它不可言传。**这就是：经验**。现在，实验不要在细节部分卡住，看看我对Smartbit API所做的相同查询：

```
{  
   "success":true,
   "transaction":{  
      "txid":"22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c",
      "hash":"22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c",
      "block":null,
      "confirmations":0,
      "version":"1",
      "locktime":1013690,
      "time":null,
      "first_seen":1477905197,
      "propagation":"1.0000",
      "double_spend":false,
      "size":372,
      "vsize":372,
      "input_amount":"0.01280443",
      "input_amount_int":1280443,
      "output_amount":"0.01274268",
      "output_amount_int":1274268,
      "fee":"0.00006175",
      "fee_int":6175,
      "fee_size":"16.59946237",
      "coinbase":false,
      "input_count":2,
      "inputs":[  
         {  
            "addresses":[  
               "n2eMqTT929pb1RDNuqEnxdaLau1rxy3efi"
            ],
            "value":"0.00100000",
            "value_int":100000,
            "txid":"820f8fd515f4dcfc8e21a96388797afe6a70b60c6764356d700cc86f2beddcd9",
            "vout":0,
            "script_sig":{  
               "asm":"3044022030b8bea478444bd52f08de33b082cde1176d3137111f506eefefa91b47b1f6bf02204f12746abd1aeac5805872d163592cf145967fa0619339a9c5348d674852ef4801 0224ec1e4c270ce373e6999eebfa01d0a7e7db3c537c026f265233350d5aab81fb",
               "hex":"473044022030b8bea478444bd52f08de33b082cde1176d3137111f506eefefa91b47b1f6bf02204f12746abd1aeac5805872d163592cf145967fa0619339a9c5348d674852ef4801210224ec1e4c270ce373e6999eebfa01d0a7e7db3c537c026f265233350d5aab81fb"
            },
            "type":"pubkeyhash",
            "witness":null,
            "sequence":4294967294
         },
         {  
            "addresses":[  
               "n3iWN6buGo6yY3HaupTa37bkvqtqSqLfhG"
            ],
            "value":"0.01180443",
            "value_int":1180443,
            "txid":"0faa264b320b82f7268c8f676b50eec9d3dfb6a8a2f53dd494355e5cb66d70a0",
            "vout":0,
            "script_sig":{  
               "asm":"3044022061b718034f876590d6d80bac77a63248b2548d934849acd02c4f4236309e853002201aded6b24f553b6902cf571276b37b12f76b75650164d8738c74469b4edd547e01 03d649294a0ca4db920a69eacd6a75cb8a38ae1b81129900621ce45e6ba3438a7b",
               "hex":"473044022061b718034f876590d6d80bac77a63248b2548d934849acd02c4f4236309e853002201aded6b24f553b6902cf571276b37b12f76b75650164d8738c74469b4edd547e012103d649294a0ca4db920a69eacd6a75cb8a38ae1b81129900621ce45e6ba3438a7b"
            },
            "type":"pubkeyhash",
            "witness":null,
            "sequence":4294967294
         }
      ],
      "output_count":2,
      "outputs":[  
         {  
            "addresses":[  
               "mzXrxNNYrVJgwNL8PGZWTJYbktrhg14kQb"
            ],
            "value":"0.00240000",
            "value_int":240000,
            "n":0,
            "script_pub_key":{  
               "asm":"OP_DUP OP_HASH160 d0965947ebb329b776328624ebde8f8b32dc6397 OP_EQUALVERIFY OP_CHECKSIG",
               "hex":"76a914d0965947ebb329b776328624ebde8f8b32dc639788ac"
            },
            "req_sigs":1,
            "type":"pubkeyhash",
            "spend_txid":null
         },
         {  
            "addresses":[  
               "myG816eAyq41xY6ZTfYTBNmE8n4aN1YM7x"
            ],
            "value":"0.01034268",
            "value_int":1034268,
            "n":1,
            "script_pub_key":{  
               "asm":"OP_DUP OP_HASH160 c2a420d34fc86cff932b8c3191549a0ddfd2b0d0 OP_EQUALVERIFY OP_CHECKSIG",
               "hex":"76a914c2a420d34fc86cff932b8c3191549a0ddfd2b0d088ac"
            },
            "req_sigs":1,
            "type":"pubkeyhash",
            "spend_txid":null
         }
      ],
      "tx_index":12079340,
      "block_index":null
   }
}
```

更加迷惑吧？你应该注意这个输出和Ninja的输出的不同点。

试一试：[**https://testnet-api.smartbit.com.au**](https://testnet-api.smartbit.com.au/v1/blockchain/tx/22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c)[ / V1 / blockchain / TX / ](https://testnet-api.smartbit.com.au/v1/blockchain/tx/22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c)[**22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c**](https://testnet-api.smartbit.com.au/v1/blockchain/tx/22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c)   mainnet(主网)：这是[**https://api.smartbit.com.au**](https://api.smartbit.com.au)

这看起来比我的更加难以迷惑，对吧？输出是json格式，您可以试试json工具，例如：[https](https://jsonformatter.curiousconcept.com/)：[//jsonformatter.curiousconcept.com/](https://jsonformatter.curiousconcept.com/)

你找到输出的交易ID吗？可以试着找找。（快捷键：Ctrl + F）。Ninja有3个位置，而Smartbit只有2个位置？这暂时不能说明什么。

#### b）构建您的交易

目前为止，我正在检查我的资金交易。现在看看我可以花费这笔交易的一种可能的方式，但在此之前，让我们弄清楚花了一笔交易的意味着什么？为什么我说交易，我不想花比特币？但比特币在哪里？现在我们的交易思维模式将在这里开始失败。但不要害怕，我聘请了该领域最好的插画师来帮助我们澄清我们的误解：

![地址](https://ask.qcloudimg.com/http-save/1162838/2x1kinifjv.jpeg)

  你有一个比特币地址，你可以把比特币转账过去的地址。  

![地址](https://ask.qcloudimg.com/http-save/1162838/tptgqoabn9.jpeg)

  现在想象的输出tx1已经被用了，所以你只能访问你的比特币tx2和tx3。因此，这些产出x2和x3未使用。如果您拥有相应的地址私钥，您仍然可以使用它们。它们被称为未使用的交易输出或**UTXO**。好吧，但你如何花费它们？通过将UTXO与其他交易的输入连接起来，然后广播该连接。这大致就是我们所说的花费比特币。 

![花费](https://ask.qcloudimg.com/http-save/1162838/7axqmv15pq.jpeg)

  我们来花费tx2，通过把它的输出连接到一个新的tx上。然后用tx2的私钥签署该连接。现在，如果您仔细聆听，您就会开始认识到交易中最重要的部分：

- 一个**输入**，
- 一个**输出**，
- 比特币**地址**，
- 以及能够花费输入的私钥的整个交易的**签名**。

我在这里使用的术语是彻头彻尾的谎言，我将是第一个在Reddit上开始诅咒作者的术语，但至少你可以理解它。现在让我告诉你什么是描述交易结构的正确方法：

| 尺寸 | 域 | 描述 |
|:----|:----|:----|
| 4字节 | 版本(Version) | 指定此交易遵循哪些规则 |
| 1-9字节（VarInt） | 输入计数器 | 包括多少输入 |
| 变量 | 输入(inputs) | 一个或多个交易输入 |
| 1-9字节（VarInt） | 输出计数器 | 包括多少个输出 |
| 变量 | 输出(outpus) | 一个或多个交易输出 |
| 4字节 | 锁定时间(locktime) | Unix时间戳或块号 |


version(版本)和locktime(锁定时间)对我们不重要，所以我们不讨论它们。input(输入)和output(输出)只是两个数字，告诉你有多少个输入和输出。但是这个计算可以很容易地通过任何机器来完成，所以它们对我们来说也不重要。等等......我告诉过你，交易只有一个输入和一个输出，我再次撒谎了。**可以有更多**，但我们大多会在我们的教程中忽略它，因为在我们的交易中只有一个输入和一个输出。那么比特币**地址**在哪里？您可以在输出中指定它。签名？在输入中。让我向你说明：

```
{  
   "in":[  
      {  
         "prev_out":{  
            "hash":"22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c",
            "n":0
         },
         "scriptSig":"3044022020ea35009d17d25b8a926675ddf0045c397d3df55b0ae115ef80db7849529b9302201f13bd2cbd1ca0a24e2c5ab28030aa9b7b3dcacf175652dad82fe9d5973f340901 0281d32f6d35b46906eb562ff8b48f4f938c077bcb29d46b0550ff5c61883d3d2d"
      }
   ],
   "out":[  
      {  
         "value":"0.00226000",
         "scriptPubKey":"OP_DUP OP_HASH160 c2a420d34fc86cff932b8c3191549a0ddfd2b0d0 OP_EQUALVERIFY OP_CHECKSIG"
      }
   ]
}
```

这是我可以花费我的资金的一种实际方式。复制粘贴它，并用您自己要创建的交易，更改具体的值，方法如下：

##### in：prev\_out：hash

你知道这是什么吗？我的交易ID。这是您发送到您的初始地址的交易。继续并改变它。

##### in：prev\_out：N

这个又是什么？再次用SMARTBIT的HTTP API检查您的资金交易：

Mainnet：[https://www.smartbit.com.au/api](https://www.smartbit.com.au/api)   

Testnet：[https://testnet.smartbit.com.au/api](https://testnet.smartbit.com.au/api)

找到交易，并选择参数选项卡。填写交易ID字段并单击GET。看看transaction:outputs。你在那里看到多少产出？我在我的交易中看到两个：

隐藏复制代码

```
"addresses": [ "mzXrxNNYrVJgwNL8PGZWTJYbktrhg14kQb" ], "value": "0.00240000", "n": 0
"addresses": [ "myG816eAyq41xY6ZTfYTBNmE8n4aN1YM7x" ], "value": "0.01034268", "n": 1
```

你也许会看到不止一个。我将跳过解释并让你知道你正在创建的交易应该是什么。`in:prev_out:n`

##### In：scriptSig

这是签名。现在就让我们不要急于填写。您在构建交易后必须签署交易。

##### out：scriptPubKey

这是我想发送我的钱的地址。好吧，有点。让我们来看一下更深层次的关系：

隐藏复制代码

```
"scriptPubKey":"OP_DUP OP_HASH160 c2a420d34fc86cff932b8c3191549a0ddfd2b0d0 OP_EQUALVERIFY OP_CHECKSIG"
```

你看到我做出的那些随机数字是否大胆？这实际上是公钥的散列，无论如何。比特币地址由版本字节组成，该版本字节标识网络在哪里使用地址以及公钥的哈希值。好吧，这可能有点令人困惑，我甚至没有告诉你什么是公钥，所以不要担心，如果你不明白，现在对我们无关紧要，这里唯一的重要的就是这个关系：   

**bitcoin address(比特币地址)= scriptPubKey + network identifier(网络标识符)**

**所以你使用mainnet还是testnet都可以，那么scriptPubKey将是相同的。** 

那么如何从比特币地址获得scriptPubKey(公钥)？我没有找到任何在线工具，所以我建立了一个小程序来帮助你。在这里下载：[https](https://github.com/nopara73/BitcoinGenie)：[//github.com/nopara73/BitcoinGenie](https://github.com/nopara73/BitcoinGenie)

运行后告诉软件：

隐藏复制代码

```
I want to know a scriptPubKey
```

它会要求你提供一个比特币地址。并返回它的scriptPubKey。如果你在testnet上，你可以指定任何地址（scriptPubkey），甚至是我在这里使用的地址。没关系，testnet的比特币毫无价值。如果您位于主网络上，您希望将其发送给自己或我，请在此处：[1LYLuYMXkCXDxSfsNoDp8FCb2mA36r29u7](https://www.smartbit.com.au/address/1LYLuYMXkCXDxSfsNoDp8FCb2mA36r29u7)

##### out：value

这比最初看起来更有趣。

假设如果你有一个有1个比特币的输入，并且你想把它发送到一个输出，为什么你还需要指定输出的值？如果你只想发送一半比特币呢？然后，您必须指定输入并指定两个值为0.5btc的输出到您要发送的地址，并将值为0.5btc的值指定回您的地址。**记住，你只能花费整数的比特币，不能花带小数的比特币！**

但看看我的：

我指定“values”:"0.00226000"。但看看我的输入：

[https:](https://testnet.smartbit.com.au/tx/22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c)[//testnet.smartbit.com.au/tx/22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c](https://testnet.smartbit.com.au/tx/22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c)

它有0.00226000btc。那么，为什么没有把我指定的0.00226000放到输出里面？剩余的（0.0024-0.00226）是什么意思？它丢了。它会消失吗？不，这部分归矿工所有。这是交易费用。那么如何计算矿工费？费用越高，交易确认的速度越快。那么你如何确保你的费用高到足以确认1-2个块？

挺简单的，只需到这里：[https:](https://bitcoinfees.21.co/api/v1/fees/recommended)[//bitcoinfees.21.co/api/v1/fees/recommended](https://bitcoinfees.21.co/api/v1/fees/recommended)   它会告诉你，你需要支付多少费用相对于你的交易规模。这是我写这篇文章时的输出结果：

隐藏复制代码

```
{"fastestFee":70,"halfHourFee":70,"hourFee":60}
```

这意味着要获得最快的费用，我必须将我的交易规模扩大70倍。普通的比特币交易约为200byte，因此我的交易费用应为70 \* 200 = 14000。哇，这是很多比特币是不是？实际上这些都不是satoshis。1 satoshi = 0.00000001比特币。所以我的14000satoshi是0.00014btc。在撰写本文时，这是0.1us。（比特币价格约为700日元，2016.10.30。）

那么你的交易费应该是多少？你应该指定什么样的out:value？

#### c）签署你的交易

现在让我们用BitcoinGenie构建我们的交易，以便我们可以将它提交给比特币网络。我警告过，不要试图玩它(不要太作，No zuo no die)，我不会处理错误，也不会处理本教程范围之外的输入。

现在再次运行Genie并告诉它：

隐藏复制代码

```
I want to create a transaction
```

此时，你可能会自己回答精灵的每个问题。 

停止阅读并单独尝试。

![暂停](https://ask.qcloudimg.com/http-save/1162838/4xryuokpso.jpeg)

```
Howdy friend, I am your Bitcoin genie. What's your wish?
<code>I want to create a transaction</code>
Great, here is a template for your transaction:

{
  "hash": "d21633ba23f70118185227be58a63527675641ad37967e2aa461559f577aec43",
  "ver": 1,
  "vin_sz": 0,
  "vout_sz": 0,
  "lock_time": 0,
  "size": 10,
  "in": [],
  "out": []
}

Specify its inputs and outputs for me
First the inputs
What is the id of the transaction that you want to spend?
<code>22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c</code>
Which output of it do you want to spend? What is its id?
<code>0</code>
Awesome, here is how your transaction looks like now:

{
  "hash": "c8f0ba9cc5083f26cafb5062304c183986c1f4602a27da0c83634af4afca41ec",
  "ver": 1,
  "vin_sz": 1,
  "vout_sz": 0,
  "lock_time": 0,
  "size": 51,
  "in": [
    {
      "prev_out": {
        "hash": "22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c",
        "n": 0
      },
      "scriptSig": ""
    }
  ],
  "out": []
}

Now let's construct the output
What is the scriptPubKey you want to send your bitcoins to?
<code>OP_DUP OP_HASH160 c2a420d34fc86cff932b8c3191549a0ddfd2b0d0 OP_EQUALVERIFY OP_CHECKSIG</code>
How much bitcoins you want to send there?
<code>0.00226</code>
Awesome, here is how your transaction looks like now:

{
  "hash": "c76361f91fc762455a3aab1b27c58369d8973e0141a9725095d318aba99bca33",
  "ver": 1,
  "vin_sz": 1,
  "vout_sz": 1,
  "lock_time": 0,
  "size": 85,
  "in": [
    {
      "prev_out": {
        "hash": "22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c",
        "n": 0
      },
      "scriptSig": ""
    }
  ],
  "out": [
    {
      "value": "0.00226000",
      "scriptPubKey": "OP_DUP OP_HASH160 c2a420d34fc86cff932b8c3191549a0ddfd2b0d0 OP_EQUALVERIFY OP_CHECKSIG"
    }
  ]
}

Now tell me your privateKey so I can sign the transaction:
<code>cTLUtfv2Sq5K1yjs5fcRmxitL51i35WmVxaCGUCbfCp722V5aMVY</code>
You signed your transaction on the TestNet
Here is how your final transaction looks like:

{
  "hash": "2a6ed4792dcefd16b7d213f2171ab75e407e53d6a4a43d1d5911b720f4a89857",
  "ver": 1,
  "vin_sz": 1,
  "vout_sz": 1,
  "lock_time": 0,
  "size": 191,
  "in": [
    {
      "prev_out": {
        "hash": "22ab5e9b703c0d4cb6023e3a1622b493adc8f83a79771c83a73dfa38ef35b07c",
        "n": 0
      },
      "scriptSig": "3044022020ea35009d17d25b8a926675ddf0045c397d3df55b0ae115ef80db7849529b9302201f13bd2cbd1ca0a24e2c5ab28030aa9b7b3dcacf175652dad82fe9d5973f340901 0281d32f6d35b46906eb562ff8b48f4f938c077bcb29d46b0550ff5c61883d3d2d"
    }
  ],
  "out": [
    {
      "value": "0.00226000",
      "scriptPubKey": "OP_DUP OP_HASH160 c2a420d34fc86cff932b8c3191549a0ddfd2b0d0 OP_EQUALVERIFY OP_CHECKSIG"
    }
  ]
}

Here is the hex of your transaction:

01000000017cb035ef38fa3da7831c77793af8c8ad93b422163a3e02b64c0d3c709b5eab22000000006a473044022020ea35009d17d25b8a926675ddf0045c397d3df55b0ae115ef80db7849529b9302201f13bd2cbd1ca0a24e2c5ab28030aa9b7b3dcacf175652dad82fe9d5973f340901210281d32f6d35b46906eb562ff8b48f4f938c077bcb29d46b0550ff5c61883d3d2dffffffff01d0720300000000001976a914c2a420d34fc86cff932b8c3191549a0ddfd2b0d088ac00000000

Press enter to exit...
```

做得好，最后我们可以广播它了！

### 4.广播到你的网络

![必须告诉每个人知道确认后](https://ask.qcloudimg.com/http-save/1162838/391wneq8sb.jpeg)

你看到你的交易的十六进制编码吗？现在请注意。这就是我们将提交给比特币网络的内容。

但首先让我们做快速检查。转到SMARTBIT的API，然后选择DECODE TRANSACTION：

Mainnet：[https://www.smartbit.com.au/api](https://www.smartbit.com.au/api)   

Testnet：[https://testnet.smartbit.com.au/api](https://testnet.smartbit.com.au/api)

复制你的十六进制。一切都很美好？太棒了，现在在同一页面上

接着PUSH TRANSACTION。

隐藏复制代码

```
Hide   Copy Code
{  
   "success":true,
   "txid":"2a6ed4792dcefd16b7d213f2171ab75e407e53d6a4a43d1d5911b720f4a89857"
}
```

如果你得到相同的输出，那么你做得很好。

查看刚刚创建的交易：[https](https://testnet.smartbit.com.au/tx/2a6ed4792dcefd16b7d213f2171ab75e407e53d6a4a43d1d5911b720f4a89857) : [//testnet.smartbit.com.au/tx/2a6ed4792dcefd16b7d213f2171ab75e407e53d6a4a43d1d5911b720f4a89857](https://testnet.smartbit.com.au/tx/2a6ed4792dcefd16b7d213f2171ab75e407e53d6a4a43d1d5911b720f4a89857)

## 结论

恭喜你，你做到了。您比其他大多数比特币爱好者更了解比特币。你现在正式成为了比特币向导。

![加入我们](https://ask.qcloudimg.com/http-save/1162838/ms042e3d5e.jpeg)

>  Quote：我们中的一个......我们中的一个......