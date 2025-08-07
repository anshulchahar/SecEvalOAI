import os
import time
import json
from openai import OpenAI
from datasets import load_dataset
from tqdm import tqdm
import pandas as pd

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL_NAME = "gpt-4o"
OUTPUT_DIR = "results"
LOG_FILE = "generation_log.txt"
SUMMARY_CSV = "results_summary.csv"

os.makedirs(OUTPUT_DIR, exist_ok=True)

dataset = load_dataset("s2e-lab/SecurityEval", split="train")

def save_log(message):
    print(message)
    with open(LOG_FILE, "a") as log_f:
        log_f.write(message + "\n")

def generate_code(prompt, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=512,
            )
            return response.choices[0].message.content
        except Exception as e:
            save_log(f"Error: {e} - Retry {attempt+1}/{retries}")
            time.sleep(delay)
    return None

results = []

save_log(f"Starting generation for {len(dataset)} prompts...")

for idx, item in enumerate(tqdm(dataset)):
    id_ = item["ID"]
    prompt = item["Prompt"]
    out_json_path = os.path.join(OUTPUT_DIR, f"{id_}.json")
    out_py_path = os.path.join(OUTPUT_DIR, f"{id_}.py")

    if os.path.exists(out_json_path) and os.path.exists(out_py_path):
        save_log(f"[{idx+1}/{len(dataset)}] Skipping ID {id_} (already done)")
        with open(out_json_path) as f:
            data = json.load(f)
        results.append({
            "ID": id_,
            "Prompt": prompt,
            "Generated_Code": data.get("generated_code", ""),
            "Status": "Skipped"
        })
        continue

    save_log(f"[{idx+1}/{len(dataset)}] Generating code for ID {id_}")

    gen_code = generate_code(prompt)
    if gen_code is None:
        save_log(f"[{idx+1}/{len(dataset)}] Failed to generate code for ID {id_}")
        results.append({
            "ID": id_,
            "Prompt": prompt,
            "Generated_Code": "",
            "Status": "Failed"
        })
        continue

    # Save JSON
    with open(out_json_path, "w") as f:
        json.dump({
            "id": id_,
            "prompt": prompt,
            "generated_code": gen_code,
            "model": MODEL_NAME,
        }, f, indent=2)

    # Save raw code to .py file
    with open(out_py_path, "w") as pyf:
        pyf.write(gen_code)

    results.append({
        "ID": id_,
        "Prompt": prompt,
        "Generated_Code": gen_code,
        "Status": "Success"
    })

    # Sleep to respect rate limits
    time.sleep(1)

# Save summary CSV
df = pd.DataFrame(results)
df.to_csv(SUMMARY_CSV, index=False)
save_log(f"Generation completed. Summary saved to {SUMMARY_CSV}")
