from datasets import load_dataset
# from googletrans import Translator
# translator = Translator()
# result = translator.translate('Mitä sinä teet')
# print(result)
dataset = load_dataset('cnn_dailymail', split='train', name='3.0.0')
print(dataset)