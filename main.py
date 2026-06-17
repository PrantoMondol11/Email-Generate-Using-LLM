import subprocess


def main():

    print("=" * 50)
    print("EMAIL GENERATION ASSISTANT")
    print("=" * 50)

    print("\nStep 1: Generating emails...")
    subprocess.run(["python", "src/generate_emails.py"])

    print("\nStep 2: Evaluating generated emails...")
    subprocess.run(["python", "src/evaluator.py"])

    print("\nStep 3: Comparing models...")
    subprocess.run(["python", "src/compare_models.py"])

    print("\n" + "=" * 50)
    print("PROJECT COMPLETED")
    print("=" * 50)

    print("\nOutputs generated:")
    print("- data/model_a_emails.json")
    print("- data/model_b_emails.json")
    print("- outputs/model_a_results.csv")
    print("- outputs/model_b_results.csv")


if __name__ == "__main__":
    main()