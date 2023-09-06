from typing import Optional
import time
import fire
from llama import Llama

LLM_LOCATION = '../llama/'

def chat(
    ckpt_dir: Optional[str] = LLM_LOCATION+'llama-2-7b-chat',
    tokenizer_path: Optional[str] = LLM_LOCATION+'tokenizer.model',
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 4,
    max_gen_len: Optional[int] = None,
):
    ll = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    print("\nThe seance will now begin.")
    summoned = input("Who would you like to summon?\n> ")
    system_directive = f"You are {summoned}"

    while True:
        question = input(f"\nWhat would you ask {summoned}?\n> ")
        print(f"\nKnuckles crack, candles flicker, and curtains gently waft as the summoning begins...")
        dialogs = [
                [
                    {"role": "system", "content": system_directive },
                    {"role": "user", "content": question}
                ]
            ]
        stime = time.process_time()

        results = ll.chat_completion(dialogs, max_gen_len=max_gen_len,temperature=temperature,top_p=top_p)
        for result in results:
            secs = str(round(time.process_time() - stime))
            print(f"{secs} seconds later {summoned}'s ghostly voice is heard:\n")
            print(result['generation']['content'].strip())

if __name__ == "__main__":
    fire.Fire(chat)
