import json
import os

data_dir = r"d:\WEBHOCTA\webhoctienganhmoingay\data\lessons"

def update_lesson(day, data):
    file_path = os.path.join(data_dir, f"day{day}.json")
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        lesson = json.load(f)
    if "tense" in lesson and "rules" in lesson["tense"] and len(lesson["tense"]["rules"]) >= 2:
        lesson["tense"]["rules"][0]["examples"] = data["grammar_affirmative"]
        lesson["tense"]["rules"][1]["examples"] = data["grammar_negative"]
    lesson["vocabulary"] = [{"id": f"v{day}_{i+1}", **v} for i, v in enumerate(data["vocabulary"])]
    lesson["listening"] = [{"id": f"l{day}_{i+1}", "sentence": s["en"], "sentenceVi": s["vi"]} for i, s in enumerate(data["listening"])]
    lesson["speaking"] = [{"id": f"s{day}_{i+1}", "sentence": s["en"], "sentenceVi": s["vi"]} for i, s in enumerate(data["speaking"])]
    lesson["writing"] = [{"id": f"w{day}_{i+1}", **w} for i, w in enumerate(data["writing"])]
    lesson["quizzes"] = [{"id": f"q{day}_{i+1}", **q} for i, q in enumerate(data["quizzes"])]
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(lesson, f, ensure_ascii=False, indent=2)

batch_data = {
    6: { # Food & Drinks
        "grammar_affirmative": [{"en": "I eat bread for breakfast.", "vi": "Tôi ăn bánh mì cho bữa sáng."}, {"en": "She drinks water.", "vi": "Cô ấy uống nước."}, {"en": "They like spicy food.", "vi": "Họ thích thức ăn cay."}],
        "grammar_negative": [{"en": "I don't drink coffee.", "vi": "Tôi không uống cà phê."}, {"en": "He doesn't eat meat.", "vi": "Anh ấy không ăn thịt."}, {"en": "We don't like soda.", "vi": "Chúng tôi không thích nước ngọt."}],
        "vocabulary": [
            {"word": "Bread", "phonetic": "/bred/", "meaning": "Bánh mì", "example": "I like bread.", "exampleVi": "Tôi thích bánh mì."},
            {"word": "Milk", "phonetic": "/mɪlk/", "meaning": "Sữa", "example": "Drink your milk.", "exampleVi": "Hãy uống sữa của bạn."},
            {"word": "Water", "phonetic": "/ˈwɑː.t̬ɚ/", "meaning": "Nước", "example": "I need water.", "exampleVi": "Tôi cần nước."},
            {"word": "Coffee", "phonetic": "/ˈkɑː.fi/", "meaning": "Cà phê", "example": "He drinks coffee.", "exampleVi": "Anh ấy uống cà phê."},
            {"word": "Tea", "phonetic": "/tiː/", "meaning": "Trà", "example": "I like green tea.", "exampleVi": "Tôi thích trà xanh."},
            {"word": "Fruit", "phonetic": "/fruːt/", "meaning": "Trái cây", "example": "Eat more fruit.", "exampleVi": "Hãy ăn thêm trái cây."},
            {"word": "Vegetable", "phonetic": "/ˈvedʒ.tə.bəl/", "meaning": "Rau củ", "example": "Vegetables are healthy.", "exampleVi": "Rau củ rất tốt cho sức khỏe."},
            {"word": "Rice", "phonetic": "/raɪs/", "meaning": "Cơm/Gạo", "example": "I eat rice every day.", "exampleVi": "Tôi ăn cơm mỗi ngày."},
            {"word": "Meat", "phonetic": "/miːt/", "meaning": "Thịt", "example": "He doesn't eat meat.", "exampleVi": "Anh ấy không ăn thịt."},
            {"word": "Egg", "phonetic": "/eɡ/", "meaning": "Trứng", "example": "I like eggs.", "exampleVi": "Tôi thích trứng."}
        ],
        "listening": [{"en": "What do you want to eat?", "vi": "Bạn muốn ăn gì?"}, {"en": "I want some rice and eggs.", "vi": "Tôi muốn ăn cơm và trứng."}, {"en": "Do you like fruit?", "vi": "Bạn có thích trái cây không?"}, {"en": "Yes, I like apples and bananas.", "vi": "Vâng, tôi thích táo và chuối."}, {"en": "I drink milk every morning.", "vi": "Tôi uống sữa mỗi sáng."}, {"en": "Coffee is too bitter for me.", "vi": "Cà phê quá đắng đối với tôi."}, {"en": "We have vegetables for dinner.", "vi": "Chúng tôi ăn rau cho bữa tối."}, {"en": "Is there any water in the fridge?", "vi": "Có nước trong tủ lạnh không?"}, {"en": "I love eating bread with butter.", "vi": "Tôi thích ăn bánh mì với bơ."}, {"en": "Let's drink some tea.", "vi": "Hãy uống một chút trà nào."}],
        "speaking": [{"en": "Are you hungry?", "vi": "Bạn có đói không?"}, {"en": "Yes, I am.", "vi": "Vâng, tôi có."}, {"en": "What would you like?", "vi": "Bạn muốn dùng gì?"}, {"en": "I'd like a sandwich.", "vi": "Tôi muốn một cái bánh sandwich."}, {"en": "Anything to drink?", "vi": "Có uống gì không?"}, {"en": "Water, please.", "vi": "Cho tôi nước nhé."}, {"en": "I don't like coffee.", "vi": "Tôi không thích cà phê."}, {"en": "I prefer tea.", "vi": "Tôi thích trà hơn."}, {"en": "Enjoy your meal!", "vi": "Chúc ngon miệng!"}, {"en": "Thank you.", "vi": "Cảm ơn bạn."}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I drink _____.", "answer": "water", "hint": "nước"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I eat _____ every day.", "answer": "rice", "hint": "cơm"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "She likes _____.", "answer": "fruit", "hint": "trái cây"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He drinks _____ in the morning.", "answer": "coffee", "hint": "cà phê"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "_____ is good for health.", "answer": "Vegetable", "hint": "Rau củ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I eat _____ for breakfast.", "answer": "bread", "hint": "bánh mì"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Do you like _____?", "answer": "milk", "hint": "sữa"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I like _____ tea.", "answer": "green", "hint": "xanh (trà...)"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I want an _____.", "answer": "egg", "hint": "quả trứng"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "He doesn't eat _____.", "answer": "meat", "hint": "thịt"}],
        "quizzes": [{"question": "'Vegetable' nghĩa là gì?", "options": ["Trái cây", "Rau củ", "Thịt", "Trứng"], "correct": 1}, {"question": "I _____ coffee.", "options": ["drink", "drinks", "drinking", "drank"], "correct": 0}, {"question": "She _____ eat meat.", "options": ["don't", "doesn't", "isn't", "not"], "correct": 1}, {"question": "Do you want _____ water?", "options": ["some", "a", "an", "any"], "correct": 0}, {"question": "They _____ like rice.", "options": ["don't", "doesn't", "isn't", "aren't"], "correct": 0}, {"question": "Apples are _____.", "options": ["fruit", "vegetable", "meat", "bread"], "correct": 0}, {"question": "'Egg' nghĩa là gì?", "options": ["Trứng", "Sữa", "Trà", "Cơm"], "correct": 0}, {"question": "I have bread _____ breakfast.", "options": ["for", "at", "in", "on"], "correct": 0}, {"question": "_____ you like tea?", "options": ["Do", "Does", "Is", "Are"], "correct": 0}, {"question": "Water is _____.", "options": ["healthy", "bitter", "sweet", "hot"], "correct": 0}]
    },
    7: { # Shopping
        "grammar_affirmative": [{"en": "I buy new clothes.", "vi": "Tôi mua quần áo mới."}, {"en": "The store sells shoes.", "vi": "Cửa hàng bán giày."}, {"en": "Prices are high here.", "vi": "Giá cả ở đây rất cao."}],
        "grammar_negative": [{"en": "I don't have enough money.", "vi": "Tôi không có đủ tiền."}, {"en": "They don't sell food here.", "vi": "Họ không bán thực phẩm ở đây."}, {"en": "It doesn't cost much.", "vi": "Nó không tốn nhiều tiền."}],
        "vocabulary": [
            {"word": "Shop", "phonetic": "/ʃɑːp/", "meaning": "Cửa hàng", "example": "Go to the shop.", "exampleVi": "Đi đến cửa hàng."},
            {"word": "Buy", "phonetic": "/baɪ/", "meaning": "Mua", "example": "I want to buy a bag.", "exampleVi": "Tôi muốn mua một cái túi."},
            {"word": "Sell", "phonetic": "/sel/", "meaning": "Bán", "example": "They sell flowers.", "exampleVi": "Họ bán hoa."},
            {"word": "Price", "phonetic": "/praɪs/", "meaning": "Giá cả", "example": "The price is low.", "exampleVi": "Giá thấp."},
            {"word": "Money", "phonetic": "/ˈmʌn.i/", "meaning": "Tiền", "example": "I have some money.", "exampleVi": "Tôi có một ít tiền."},
            {"word": "Cost", "phonetic": "/kɑːst/", "meaning": "Giá/Tốn phí", "example": "How much does it cost?", "exampleVi": "Nó giá bao nhiêu?"},
            {"word": "Cheap", "phonetic": "/tʃiːp/", "meaning": "Rẻ", "example": "This is cheap.", "exampleVi": "Cái này rẻ."},
            {"word": "Expensive", "phonetic": "/ɪkˈspen.sɪv/", "meaning": "Đắt", "example": "It is too expensive.", "exampleVi": "Nó quá đắt."},
            {"word": "Store", "phonetic": "/stɔːr/", "meaning": "Cửa hàng/Kho", "example": "A big store.", "exampleVi": "Một cửa hàng lớn."},
            {"word": "Market", "phonetic": "/ˈmɑːr.kɪt/", "meaning": "Chợ", "example": "I go to the market.", "exampleVi": "Tôi đi chợ."}
        ],
        "listening": [{"en": "I need to go shopping.", "vi": "Tôi cần đi mua sắm."}, {"en": "Where is the nearest market?", "vi": "Chợ gần nhất ở đâu?"}, {"en": "How much is this shirt?", "vi": "Cái áo sơ mi này giá bao nhiêu?"}, {"en": "It is ten dollars.", "vi": "Nó giá mười đô la."}, {"en": "That is very cheap.", "vi": "Cái đó rất rẻ."}, {"en": "I want to buy these shoes.", "vi": "Tôi muốn mua đôi giày này."}, {"en": "Do you have change?", "vi": "Bạn có tiền lẻ không?"}, {"en": "The shop is closed today.", "vi": "Cửa hàng đóng cửa hôm nay."}, {"en": "Everything is on sale.", "vi": "Mọi thứ đang được giảm giá."}, {"en": "I don't have enough money.", "vi": "Tôi không có đủ tiền."}],
        "speaking": [{"en": "How much is it?", "vi": "Nó giá bao nhiêu?"}, {"en": "It's 20 dollars.", "vi": "Nó giá 20 đô la."}, {"en": "Can I have a discount?", "vi": "Tôi có được giảm giá không?"}, {"en": "No, sorry.", "vi": "Không, xin lỗi."}, {"en": "I'll take it.", "vi": "Tôi sẽ lấy nó."}, {"en": "Do you accept credit cards?", "vi": "Bạn có chấp nhận thẻ tín dụng không?"}, {"en": "Yes, we do.", "vi": "Vâng, chúng tôi có."}, {"en": "Here is your receipt.", "vi": "Đây là hóa đơn của bạn."}, {"en": "Thank you.", "vi": "Cảm ơn bạn."}, {"en": "Have a nice day!", "vi": "Chúc một ngày tốt lành!"}],
        "writing": [{"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "How _____ is it?", "answer": "much", "hint": "bao nhiêu (giá)"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I want to _____ this.", "answer": "buy", "hint": "mua"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "The _____ is too high.", "answer": "price", "hint": "giá cả"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "It is very _____.", "answer": "cheap", "hint": "rẻ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "It is too _____.", "answer": "expensive", "hint": "đắt"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "I don't have ____.", "answer": "money", "hint": "tiền"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "They _____ flowers.", "answer": "sell", "hint": "bán"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Go to the _____.", "answer": "shop", "hint": "cửa hàng"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "Where is the _____?", "answer": "market", "hint": "chợ"}, {"type": "fill-blank", "instruction": "Điền vào chỗ trống", "question": "How much does it _____?", "answer": "cost", "hint": "giá/tốn"}],
        "quizzes": [{"question": "'Expensive' nghĩa là gì?", "options": ["Rẻ", "Đắt", "Đẹp", "Xấu"], "correct": 1}, {"question": "How much _____ it cost?", "options": ["do", "does", "is", "are"], "correct": 1}, {"question": "I want to _____ a bag.", "options": ["buy", "sell", "give", "take"], "correct": 0}, {"question": "The shop _____ shoes.", "options": ["buy", "sell", "sells", "selling"], "correct": 2}, {"question": "It is _____ cheap.", "options": ["very", "too", "so", "all"], "correct": 0}, {"question": "Do you have _____ money?", "options": ["some", "any", "a", "an"], "correct": 1}, {"question": "_____ price is low.", "options": ["The", "A", "An", "Some"], "correct": 0}, {"question": "'Cheap' nghĩa là gì?", "options": ["Rẻ", "Đắt", "Cao", "Thấp"], "correct": 0}, {"question": "They _____ sell food.", "options": ["don't", "doesn't", "isn't", "not"], "correct": 0}, {"question": "Everything is _____ sale.", "options": ["on", "at", "in", "for"], "correct": 0}]
    }
}

for d in batch_data:
    update_lesson(d, batch_data[d])
print("Batch 2 updated successfully.")
