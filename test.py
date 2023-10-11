from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
 
# チャットボット指定
chatbot = ChatBot('ja_test')
 
# 訓練準備
trainer = ChatterBotCorpusTrainer(chatbot)
# 日本語で訓練
trainer.train('chatterbot.corpus.japanese')

# 回答を取得して表示
#res = chatbot.get_response('出身はどちらですか')
res = chatbot.get_response('神奈川の県庁所在地')
print(res)