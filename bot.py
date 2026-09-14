import telebot
from telebot import types

# Token và Admin ID của bạn
TOKEN = "8669420885:AAH95FXO5CbGVvyApmui-8On0uoDw4WFmp0"
ADMIN_ID = 7550929812

bot = telebot.TeleBot(TOKEN)

# Thông tin Ngân hàng chuyển khoản nạp tiền
BANK_ID = "MB"          
ACCOUNT_NO = "0862446911" 
ACCOUNT_NAME = "NGUYEN QUOC BAO"

# KHO HÀNG TỰ ĐỘNG (Lưu trữ Key hoặc Link tải theo mã sản phẩm ID)
product_stock = {
    "filza_1": ["KEY_AIMNECK_VIP_01", "KEY_AIMNECK_VIP_02"],
    "proxy_1": ["PROXY_1NGAY_ABC1", "PROXY_1NGAY_ABC2"],
    "ffhax_1": ["https://example.com/download/ffhax-1day"]
}

# Hệ thống danh mục và sản phẩm chi tiết
shop_categories = {
    "aimlock": {
        "title": "🎯 **DANH MỤC SẢN PHẨM: AIMLOCK**",
        "items": [
            {"id": "aim_1", "name": "AimLock Sensi 1.0", "price": 50000, "price_str": "50.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "aim_2", "name": "AimLock Utral 2.0", "price": 100000, "price_str": "100.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "aim_3", "name": "AimLock Premium 3.0", "price": 150000, "price_str": "150.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "aim_4", "name": "AimLock LuxVip 4.0", "price": 200000, "price_str": "200.000đ", "image": "https://via.placeholder.com/400"}
        ]
    },
    "aim_filza": {
        "title": "📂 **DANH MỤC SẢN PHẨM: AIM FILZA**",
        "items": [
            {"id": "filza_1", "name": "AimNeck", "price": 70000, "price_str": "70.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "filza_2", "name": "AimBody", "price": 70000, "price_str": "70.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "filza_3", "name": "AimChest", "price": 70000, "price_str": "70.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "filza_4", "name": "AimDrag", "price": 70000, "price_str": "70.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "filza_5", "name": "AimMagic", "price": 70000, "price_str": "70.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "filza_6", "name": "AimLock FFTh", "price": 150000, "price_str": "150.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "filza_7", "name": "AimLock FFM", "price": 150000, "price_str": "150.000đ", "image": "https://via.placeholder.com/400"}
        ]
    },
    "slotvip": {
        "title": "🎰 **DANH MỤC SẢN PHẨM: SLOTVIP**",
        "items": [
            {"id": "slot_1", "name": "SlotVip Hack 1 Ngày", "price": 30000, "price_str": "30.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "slot_2", "name": "SlotVip Hack 1 Tháng", "price": 250000, "price_str": "250.000đ", "image": "https://via.placeholder.com/400"}
        ]
    },
    "proxy": {
        "title": "🌐 **DANH MỤC SẢN PHẨM: PROXY**",
        "items": [
            {"id": "proxy_1", "name": "Proxy 1 Ngày", "price": 20000, "price_str": "20.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "proxy_2", "name": "Proxy 7 Ngày", "price": 70000, "price_str": "70.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "proxy_3", "name": "Proxy 30 Ngày", "price": 150000, "price_str": "150.000đ", "image": "https://via.placeholder.com/400"}
        ]
    },
    "modskin": {
        "title": "👕 **DANH MỤC SẢN PHẨM: MODSKIN**",
        "items": [
            {"id": "mod_1", "name": "Modskin FF Full Hiệu Ứng", "price": 80000, "price_str": "80.000đ", "image": "https://via.placeholder.com/400"}
        ]
    },
    "menu_item": {
        "title": "📜 **DANH MỤC SẢN PHẨM: MENU**",
        "items": [
            {"id": "menu_ffhax", "name": "FF Hax (Chọn gói)", "price": 0, "price_str": "Từ 30.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "menu_flourite", "name": "Flourite (Chọn gói)", "price": 0, "price_str": "Từ 90.000đ", "image": "https://via.placeholder.com/400"},
            {"id": "menu_migul", "name": "Migul (Chọn gói)", "price": 0, "price_str": "Từ 50.000đ", "image": "https://via.placeholder.com/400"}
        ]
    }
}

menu_sub_items = {
    "menu_ffhax": [
        {"id": "ffhax_1", "name": "FF Hax - 1 Ngày", "price": 30000, "price_str": "30.000đ", "image": "https://via.placeholder.com/400"},
        {"id": "ffhax_7", "name": "FF Hax - 7 Ngày", "price": 80000, "price_str": "80.000đ", "image": "https://via.placeholder.com/400"},
        {"id": "ffhax_30", "name": "FF Hax - 30 Ngày", "price": 180000, "price_str": "180.000đ", "image": "https://via.placeholder.com/400"}
    ],
    "menu_flourite": [
        {"id": "flou_1", "name": "Flourite - 1 Ngày", "price": 90000, "price_str": "90.000đ", "image": "https://via.placeholder.com/400"},
        {"id": "flou_7", "name": "Flourite - 7 Ngày", "price": 250000, "price_str": "250.000đ", "image": "https://via.placeholder.com/400"},
        {"id": "flou_30", "name": "Flourite - 30 Ngày", "price": 450000, "price_str": "450.000đ", "image": "https://via.placeholder.com/400"}
    ],
    "menu_migul": [
        {"id": "mig_1", "name": "Migul - 1 Ngày", "price": 50000, "price_str": "50.000đ", "image": "https://via.placeholder.com/400"},
        {"id": "mig_7", "name": "Migul - 7 Ngày", "price": 150000, "price_str": "150.000đ", "image": "https://via.placeholder.com/400"},
        {"id": "mig_30", "name": "Migul - 30 Ngày", "price": 350000, "price_str": "350.000đ", "image": "https://via.placeholder.com/400"}
    ]
}

deposit_packages = {
    "dep_50k": {"amount": 50000, "label": "Nạp 50.000đ"},
    "dep_100k": {"amount": 100000, "label": "Nạp 100.000đ"},
    "dep_200k": {"amount": 200000, "label": "Nạp 200.000đ"},
    "dep_500k": {"amount": 500000, "label": "Nạp 500.000đ"}
}

user_cart = {}
user_balances = {}
user_total_deposit = {} # Lưu tổng tiền nạp của khách

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Các nút danh mục sản phẩm dịch vụ chính (đã thêm icon)
    btn1 = types.InlineKeyboardButton("🎯 AIMLOCK", callback_data="cat_aimlock")
    btn2 = types.InlineKeyboardButton("📂 AIM FILZA", callback_data="cat_aim_filza")
    btn3 = types.InlineKeyboardButton("🎰 SLOTVIP", callback_data="cat_slotvip")
    btn4 = types.InlineKeyboardButton("🌐 PROXY", callback_data="cat_proxy")
    btn5 = types.InlineKeyboardButton("👕 MODSKIN", callback_data="cat_modskin")
    btn6 = types.InlineKeyboardButton("📜 MENU", callback_data="cat_menu_item")
    
    btn_deposit = types.InlineKeyboardButton("💳 Nạp Tiền Vào Ví", callback_data="menu_deposit")
    btn_support = types.InlineKeyboardButton("🎧 Hỗ trợ / Liên hệ", url="https://t.me/lionVnIos")
    
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)
    markup.add(btn_deposit, btn_support)
    
    current_bal = user_balances.get(chat_id, 0)
    total_dep = user_total_deposit.get(chat_id, 0)
    
    welcome_text = (
        "👑 **CHÀO MỪNG BẠN ĐẾN VỚI BOT AUTO BÁN HACK VIP** ✅\n\n"
        "╭────────────────────────╮\n"
        "│ 📢 **Kênh thông báo:** https://t.me/+0XZ9MT3yDXw0NTll\n"
        "│ 👨‍💻 **Admin:** @lionVnIos\n"
        "╰────────────────────────╯\n"
        "➖➖➖➖➖➖➖➖➖➖➖➖\n"
        f"🇻 **Tổng nạp:** `{total_dep:,}đ`\n"
        f"💰 **Tổng nạp tháng:** `{total_dep:,}đ`\n"
        f"🏛️ **Số dư:** `{current_bal:,}đ`\n\n"
        "👇 **Vui lòng chọn danh mục dịch vụ bên dưới:**"
    )
    
    bot.send_message(chat_id, welcome_text, parse_mode="Markdown", reply_markup=markup, disable_web_page_preview=True)

@bot.message_handler(commands=['congti'])
def add_balance_to_user(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        parts = message.text.replace("/congti", "").strip().split()
        if len(parts) < 2:
            bot.reply_to(message, "⚠️ Sai cú pháp! Dùng: `/congti ID_Khách Số_tiền`", parse_mode="Markdown")
            return
        
        target_chat_id = int(parts[0])
        amount = int(parts[1])
        
        current = user_balances.get(target_chat_id, 0)
        user_balances[target_chat_id] = current + amount
        
        # Cộng dồn tổng nạp
        current_total = user_total_deposit.get(target_chat_id, 0)
        user_total_deposit[target_chat_id] = current_total + amount
        
        bot.reply_to(message, f"✅ Đã cộng `{amount:,}đ` cho ID: `{target_chat_id}`.\nVí hiện tại của khách: `{user_balances[target_chat_id]:,}đ`", parse_mode="Markdown")
        bot.send_message(target_chat_id, f"🎉 **NẠP TIỀN THÀNH CÔNG!**\nTài khoản được cộng thêm: **{amount:,}đ**\n💰 Số dư ví: **{user_balances[target_chat_id]:,}đ**", parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi: {str(e)}")

@bot.message_handler(commands=['kho'])
def manage_stock(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        content = message.text.replace("/kho", "").strip()
        if "|" not in content:
            bot.reply_to(message, "⚠️ Sai cú pháp! Dùng: `/kho ID_Sản_Phẩm | Key_Hoặc_Link`", parse_mode="Markdown")
            return
        
        parts = content.split("|")
        item_id = parts[0].strip()
        item_value = parts[1].strip()
        
        if item_id not in product_stock:
            product_stock[item_id] = []
        
        product_stock[item_id].append(item_value)
        bot.reply_to(message, f"✅ Đã thêm vào kho ID: `{item_id}`\n📦 Nội dung: `{item_value}`\n📊 Tổng kho: `{len(product_stock[item_id])}`", parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi kho hàng: {str(e)}")

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    
    if call.data.startswith("submenu_"):
        sub_key = call.data.replace("submenu_", "")
        items = menu_sub_items.get(sub_key)
        if not items:
            bot.answer_callback_query(call.id, "Mục không tồn tại!")
            return
            
        text = f"📜 **CHI TIẾT GÓI LỰA CHỌN**\n\n📋 **Danh sách gói:**\n"
        for idx, itm in enumerate(items, 1):
            text += f"{idx}. **{itm['name']}** — `{itm['price_str']}`\n"
            
        markup = types.InlineKeyboardMarkup(row_width=1)
        for itm in items:
            markup.add(types.InlineKeyboardButton(f"🛒 Mua {itm['name']} ({itm['price_str']})", callback_data=f"buy_sub_{sub_key}_{itm['id']}"))
        markup.add(types.InlineKeyboardButton("⬅️ Quay lại danh mục MENU", callback_data="cat_menu_item"))
        
        try:
            bot.edit_message_text(text, chat_id=chat_id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        except Exception:
            pass

    elif call.data.startswith("buy_sub_"):
        parts = call.data.split("_")
        if len(parts) >= 4:
            sub_key = parts[2]
            item_id = "_".join(parts[3:])
            items = menu_sub_items.get(sub_key)
            selected_item = None
            if items:
                for itm in items:
                    if itm['id'] == item_id:
                        selected_item = itm
                        break
            if not selected_item:
                bot.answer_callback_query(call.id, "Sản phẩm không tồn tại!")
                return
                
            process_purchase(call, selected_item)

    elif call.data.startswith("cat_"):
        cat_key = call.data.replace("cat_", "")
        category = shop_categories.get(cat_key)
        
        if not category:
            bot.answer_callback_query(call.id, "Danh mục không tồn tại!")
            return
            
        text = f"{category['title']}\n\n📋 **Danh sách sản phẩm chi tiết:**\n"
        for idx, item in enumerate(category['items'], 1):
            text += f"{idx}. **{item['name']}** — `{item['price_str']}`\n"
            
        markup = types.InlineKeyboardMarkup(row_width=1)
        
        if cat_key == "menu_item":
            markup.add(types.InlineKeyboardButton("🔹 FF Hax", callback_data="submenu_menu_ffhax"))
            markup.add(types.InlineKeyboardButton("🔹 Flourite", callback_data="submenu_menu_flourite"))
            markup.add(types.InlineKeyboardButton("🔹 Migul", callback_data="submenu_menu_migul"))
        else:
            for item in category['items']:
                markup.add(types.InlineKeyboardButton(f"🛒 Mua {item['name']} ({item['price_str']})", callback_data=f"buy_{cat_key}_{item['id']}"))
                
        markup.add(types.InlineKeyboardButton("⬅️ Quay lại Menu Chính", callback_data="back_home"))
        
        try:
            bot.edit_message_text(text, chat_id=chat_id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        except Exception:
            pass

    elif call.data.startswith("buy_"):
        parts = call.data.split("_")
        if len(parts) >= 3:
            cat_key = parts[1]
            item_id = "_".join(parts[2:])
            
            category = shop_categories.get(cat_key)
            selected_item = None
            if category:
                for itm in category['items']:
                    if itm['id'] == item_id:
                        selected_item = itm
                        break
                        
            if not selected_item:
                bot.answer_callback_query(call.id, "Sản phẩm không tồn tại!")
                return
                
            process_purchase(call, selected_item)

    elif call.data == "menu_deposit":
        markup = types.InlineKeyboardMarkup(row_width=2)
        for key, dep in deposit_packages.items():
            markup.add(types.InlineKeyboardButton(dep['label'], callback_data=f"dep_{key}"))
        markup.add(types.InlineKeyboardButton("⬅️ Quay lại Menu Chính", callback_data="back_home"))
        
        try:
            bot.edit_message_text(
                "💳 **CHỌN MỨC GIÁ NẠP TIỀN:**\nVui lòng chọn số tiền bạn muốn nạp vào ví:",
                chat_id=chat_id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup
            )
        except Exception:
            pass

    elif call.data.startswith("dep_dep_"):
        pkg_key = call.data.replace("dep_", "")
        dep_info = deposit_packages.get(pkg_key)
        if not dep_info:
            return
            
        amount = dep_info['amount']
        user_cart[chat_id] = {"type": "deposit", "amount": amount}
        
        add_info = f"NAP {chat_id}"
        qr_url = f"https://img.vietqr.io/image/{BANK_ID}-{ACCOUNT_NO}-compact2.png?amount={amount}&addInfo={add_info}&accountName={ACCOUNT_NAME}"
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("✅ Đã Chuyển Khoản Xong", callback_data="confirm_deposit"))
        markup.add(types.InlineKeyboardButton("⬅️ Chọn lại mệnh giá", callback_data="menu_deposit"))
        
        caption_text = (
            "🏦 **MÃ QR QUÉT NHANH CHUYỂN KHOẢN**\n"
            "--------------------------------------------------\n"
            f"🔹 Ngân hàng: **MB Bank**\n"
            f"🔹 Số tài khoản: `{ACCOUNT_NO}`\n"
            f"🔹 Chủ tài khoản: **{ACCOUNT_NAME}**\n"
            f"🔹 Số tiền: **{amount:,}đ**\n"
            f"🔹 Nội dung chuyển: `{add_info}`\n"
            "--------------------------------------------------\n"
            "💡 *Mở app ngân hàng quét mã QR bên trên để tự động điền thông tin và số tiền chính xác!*"
        )
        
        try:
            bot.delete_message(chat_id, call.message.message_id)
            bot.send_photo(chat_id, photo=qr_url, caption=caption_text, parse_mode="Markdown", reply_markup=markup)
        except Exception:
            bot.send_message(chat_id, caption_text, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "confirm_deposit":
        dep_data = user_cart.get(chat_id)
        if not dep_data or dep_data.get("type") != "deposit":
            bot.answer_callback_query(call.id, "Phiên giao dịch hết hạn!", show_alert=True)
            return
            
        amount = dep_data["amount"]
        try:
            bot.delete_message(chat_id, call.message.message_id)
        except:
            pass
            
        bot.send_message(
            chat_id,
            "⏳ **ĐÃ GỬI YÊU CẦU XÁC NHẬN!**\nHệ thống đã gửi thông tin đến Admin. Số dư sẽ được cộng ngay khi xác nhận.",
            parse_mode="Markdown"
        )
        
        admin_notification = (
            f"🔔 **CÓ YÊU CẦU NẠP TIỀN MỚI!**\n\n"
            f"👤 Khách: {call.from_user.first_name} (@{call.from_user.username or 'Không có'})\n"
            f"🆔 ID Khách: `{chat_id}`\n"
            f"💰 Số tiền: **{amount:,}đ**\n\n"
            f"👉 Lệnh cộng tiền: `/congti {chat_id} {amount}`"
        )
        bot.send_message(ADMIN_ID, admin_notification, parse_mode="Markdown")

    elif call.data == "back_home":
        try:
            bot.delete_message(chat_id, call.message.message_id)
        except:
            pass
        send_welcome(call.message)

def process_purchase(call, item):
    chat_id = call.message.chat.id
    price = item["price"]
    current_balance = user_balances.get(chat_id, 0)
    
    if current_balance < price:
        bot.answer_callback_query(call.id, f"❌ Số dư không đủ! Bạn còn {current_balance:,}đ, cần {item['price_str']}.", show_alert=True)
        return
        
    stock_list = product_stock.get(item["id"], [])
    if len(stock_list) <= 0:
        bot.answer_callback_query(call.id, "❌ Sản phẩm này tạm hết hàng trong kho! Vui lòng quay lại sau.", show_alert=True)
        return
        
    user_balances[chat_id] = current_balance - price
    item_delivered = stock_list.pop(0)
    
    try:
        bot.delete_message(chat_id, call.message.message_id)
    except:
        pass
        
    success_text = (
        f"🎉 **MUA HÀNG THÀNH CÔNG!**\n"
        f"--------------------------------------------------\n"
        f"🛍️ Sản phẩm: **{item['name']}**\n"
        f"💰 Đã trừ: **{item['price_str']}**\n"
        f"💳 Số dư ví còn lại: **{user_balances[chat_id]:,}đ**\n"
        f"--------------------------------------------------\n"
        f"📦 **THÔNG TIN / KEY / LINK TẢI CỦA BẠN:**\n"
        f"`{item_delivered}`\n"
        f"--------------------------------------------------\n"
        f"⚠️ *Vui lòng lưu lại thông tin trên. Cảm ơn bạn đã ủng hộ shop!*"
    )
    bot.send_message(chat_id, success_text, parse_mode="Markdown")
    
    admin_log = (
        f"🤖 **[AUTO-GIAO HÀNG THÀNH CÔNG]**\n\n"
        f"🛍️ Sản phẩm: **{item['name']}**\n"
        f"💰 Giá: {item['price_str']}\n"
        f"🔑 Đã xuất kho: `{item_delivered}`\n"
        f"👤 Khách: {call.from_user.first_name} (ID: `{chat_id}`)"
    )
    bot.send_message(ADMIN_ID, admin_log, parse_mode="Markdown")

print("Bot bán hàng tự động đang chạy...")
bot.infinity_polling()
