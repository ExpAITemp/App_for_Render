# Мінімальний калькулятор (Gradio)

Простий вебкалькулятор на Python: обчислює суму та різницю двох чисел `a` і `b`.

## Локальний запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Застосунок буде доступний на `http://127.0.0.1:7860` (або на порту з змінної середовища `PORT`).

## Деплой

Застосунок задеплоєно на [Render](https://render.com) як Web Service (Python runtime):

- Build command: `pip install -r requirements.txt`
- Start command: `python app.py`

URL опублікованого застосунку: `<додати після деплою>`
