import os

import gradio as gr


def parse_number(value):
    """Перетворює введений текст у float. Порожнє або некоректне значення -> None."""
    if value is None:
        return None
    text = str(value).strip()
    if text == "":
        return None
    try:
        return float(text)
    except ValueError:
        return None


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculate(a, b):
    a_num = parse_number(a)
    b_num = parse_number(b)

    if a_num is None or b_num is None:
        return "Помилка: введіть коректні числа у поля a та b.", ""

    sum_result = add(a_num, b_num)
    diff_result = subtract(a_num, b_num)
    return str(sum_result), str(diff_result)


with gr.Blocks(title="Калькулятор") as demo:
    gr.Markdown("# Мінімальний калькулятор")
    with gr.Row():
        a_input = gr.Textbox(label="a")
        b_input = gr.Textbox(label="b")

    calculate_button = gr.Button("Обчислити")

    with gr.Row():
        sum_output = gr.Textbox(label="Сума (a + b)")
        diff_output = gr.Textbox(label="Різниця (a - b)")

    calculate_button.click(
        fn=calculate,
        inputs=[a_input, b_input],
        outputs=[sum_output, diff_output],
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
