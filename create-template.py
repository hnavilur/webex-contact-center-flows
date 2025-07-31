import os
import json
import openai

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():

    print("[1/5] Locating files...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    unfilled_path = os.path.join(base_dir, 'template-body-unfilled-subflow.json')
    readme_path = os.path.join(base_dir, 'subflow-register-scheduled_callback-template', 'README.md')
    flow_json_path = os.path.join(base_dir, 'subflow-register-scheduled_callback-template', 'RegisteredScheduledCallback_Template.json')
    output_path = os.path.join(base_dir, 'subflow-register-scheduled_callback-template', 'template-body-filled.json')

    print("[2/5] Reading template-body-unfilled.json...")
    template_unfilled = read_file(unfilled_path)
    print("[3/5] Reading README.md and Predictive_Progressive_Campaign_Template.json...")
    readme = read_file(readme_path)
    flow_json = read_file(flow_json_path)

    print("[4/5] Building prompt and sending request to OpenAI API...")
    prompt = '''You will be provided with a JSON file called template-body-unfilled. Create a template body filled JSON by using the fields inside the markdown file provided. Use the "details" section for the details field, and fill the other fields based on the heading and subheadings paradigms. the details field needs to have everything, like pre-requisites, activities used etc. Provide the completed JSON.'''

    messages = [
        {"role": "system", "content": "You are a helpful file generation assistant that generates filled template JSONs for Webex Contact Center flows."},
        {"role": "user", "content": prompt},
        {"role": "user", "content": f"TEMPLATE=\n{template_unfilled}"},
        {"role": "user", "content": f"README=\n{readme}"},
        {"role": "user", "content": f"FLOW_JSON=\n{flow_json}"}
    ]

    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
        max_tokens=2048,
        temperature=0.2
    )

    print("[5/5] Writing output to template-body-filled.json...")
    output_json = response.choices[0].message.content
    try:
        parsed = json.loads(output_json)
        output_json = json.dumps(parsed, indent=2)
    except Exception:
        pass
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_json)
    print(f"✅ Generated {output_path}")

if __name__ == "__main__":
    main()
