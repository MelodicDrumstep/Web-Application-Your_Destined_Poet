# 安装以下2个包方便文字处理和模型生成
# !pip install -q simplet5
# !pip install -q chinese-converter

# 具体代码
import torch
from simplet5 import SimpleT5
from transformers import T5Tokenizer, T5ForConditionalGeneration
import chinese_converter

MODELS = {
    '2023-v2': ("./poet_gene/chinese-poem-t5-v2", 32)
}
MODEL_VERSION = '2023-v2'  # @param ["2023-v2", "2022-v1"]
# Huggingface model card
MODEL_PATH = MODELS[MODEL_VERSION][0]
class PoemModel(SimpleT5):
  def __init__(self) -> None:
    super().__init__()
    self.device = torch.device("cpu")

  def load_my_model(self):
    self.tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
    self.model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)


AUTHOR_PROMPT = "模仿："
TITLE_PROMPT = "作诗："
EOS_TOKEN = '</s>'

poem_model = PoemModel()
poem_model.load_my_model()
poem_model.model = poem_model.model.to('cpu')

MAX_AUTHOR_CHAR = 4
MAX_TITLE_CHAR = 12
MIN_CONTENT_CHAR = 10
MAX_CONTENT_CHAR = MODELS[MODEL_VERSION][1]

def _poem(title_str, opt_author=None, model=poem_model,
         is_input_traditional_chinese=False,
         num_beams=2, _print=True):
  model.model = model.model.to('cpu')
  if opt_author:
    in_request = TITLE_PROMPT + title_str[:MAX_TITLE_CHAR] + EOS_TOKEN + AUTHOR_PROMPT + opt_author[:MAX_AUTHOR_CHAR]
  else:
    in_request = TITLE_PROMPT + title_str[:MAX_TITLE_CHAR]
  if is_input_traditional_chinese:
    in_request = chinese_converter.to_simplified(in_request)
  out = model.predict(in_request,
                      max_length=MAX_CONTENT_CHAR,
                      num_beams=num_beams)[0].replace(",", "，")
  if is_input_traditional_chinese:
    out = chinese_converter.to_traditional(out)
    res = f"標題： {in_request.replace('</s>', ' ')}\n詩歌： {out}"
    if _print:
        print(res)
    return res
  else:
    res = f"标题： {in_request.replace('</s>', ' ')}\n诗歌： {out}"
    if _print:
        print(res)
    return res

from typing import Optional
def generate_poem_with_tile_and_poet(title: str, poet: Optional[str] = None, num_beams: int = 50):
    res_in_str = _poem(title, poet, num_beams=num_beams, _print=False)
    strs = res_in_str.replace("：", "\n").split("\n")
    return strs[-1].strip()


# if __name__ == '__main__':
#     poem = generate_poem_with_tile_and_poet("雨过", "苏轼")
#     print(poem)