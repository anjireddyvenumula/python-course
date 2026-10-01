# prompt_builder.py
# Practice: classes, dataclasses, f-strings, lists and dictionaries.
# Builds the kind of message list you send to a chat AI model, without calling an API.

from dataclasses import dataclass, field


@dataclass
class PromptTemplate:
    name: str
    template: str
    required: list = field(default_factory=list)

    def render(self, **values):
        missing = [key for key in self.required if key not in values]
        if missing:
            raise ValueError(f"Missing values for {self.name}: {missing}")
        return self.template.format(**values)


SUMMARIZE = PromptTemplate(
    name="summarize",
    template="Summarize the following text in {sentences} sentences:\n\n{text}",
    required=["sentences", "text"],
)

TRANSLATE = PromptTemplate(
    name="translate",
    template="Translate this into {language}: {text}",
    required=["language", "text"],
)


def build_messages(system, user_prompt, history=None):
    messages = [{"role": "system", "content": system}]
    messages.extend(history or [])
    messages.append({"role": "user", "content": user_prompt})
    return messages


def estimate_tokens(messages):
    """Rough estimate: about 4 characters per token."""
    return sum(len(m["content"]) for m in messages) // 4


if __name__ == "__main__":
    prompt = SUMMARIZE.render(sentences=2, text="Python is a versatile language...")
    messages = build_messages("You are a concise assistant.", prompt)
    for message in messages:
        print(f"{message['role'].upper()}: {message['content']}\n")
    print("Estimated tokens:", estimate_tokens(messages))

    try:
        TRANSLATE.render(text="Hello")
    except ValueError as error:
        print("Error:", error)

# Try it:
# 1. Add a CLASSIFY template that asks for one of several labels.
# 2. Add previous messages as history and check how the token estimate grows.
