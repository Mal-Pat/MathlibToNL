from openai import OpenAI

client = OpenAI(api_key="")

def translate_lean_code_to_text(lean_code: str):
    
    response = client.chat.completions.create( 
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates formal mathematical theorems in Lean 4 into natural language."},
            {"role": "user", "content": f"Translate the following Lean 4 code into natural language. Give a clear and short answer in natural language: {lean_code}"}
            ] 
        )

    translated_text = response.choices[0].message.content
    print("Translation Output:", translated_text)



lean_code_example = "theorem exists_forall_hasDerivWithinAt_Icc_eq :\n    ∀ {E : Type u_1} [inst : NormedAddCommGroup E] [inst_1 : NormedSpace ℝ E] [inst_2 : CompleteSpace E] {v : ℝ → E → E}\n      {tMin t₀ tMax : ℝ} (x₀ : E) {C R : ℝ} {L : NNReal},\n      IsPicardLindelof v tMin t₀ tMax x₀ L R C →\n        ∃ f, f t₀ = x₀ ∧ ∀ t ∈ Set.Icc tMin tMax, HasDerivWithinAt f (v t (f t)) (Set.Icc tMin tMax) t :=\n  by sorry"

translate_lean_code_to_text(lean_code_example)