import openai

# ตั้งค่า API key ของคุณ
openai.api_key = "sk-gpkpEzlVsfezAccpaqhw-qERTjU0cOBfy84vEKbafzT3BlbkFJ9sPPaIpYzQej9PygeM-ETxvGiJ9cJV6RY5rbW731IA"

# เรียกใช้ Chat Completion
completion = openai.ChatCompletion.create(
    model="gpt-4o-mini",  # ใช้โมเดลที่ถูกต้อง
    messages=[
        {"role": "system", "content": "You are Mie from the story 'Sukinako ga Megane wo Wasureta.' You often forget your glasses, and you are a bit clumsy and shy, but also very kind and polite. Respond as Mie when you are talking to Komura."},
        {
            "role": "user",
            "content": "สวัสดีคุณมิเอะซัง."
        }
    ]
)

# แสดงผลลัพธ์
print(completion.choices[0].message['content'])
