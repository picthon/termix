from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
**- اهـلا عـزيـزي {}
اهـلاً بـك فـي Extract String Session
يـعـمل هـذا الـبوت لـمـساعـدتـك بـطـريقـة سـهله للـحصـول علـى كـود تـيـرمكس او كـود بـايـࢪوجـرام
Dev: @a_t_9
**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("ابـدا بـأسـتخـدام كـود", callback_data="generate")],
        [InlineKeyboardButton(text=" رجــوع ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("ابـدا بـأسـتخـدام كـود", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("ابـدا بـأسـتخـدام كـود", callback_data="generate")],
        
        [
            InlineKeyboardButton("طريقة الاستخدام؟", callback_data="help"),
            InlineKeyboardButton("- حول البوت", callback_data="about")
        ],
        
    ]

    # Help Message
    HELP = """
**- هــذه هـي قـائـمة اسـتـخـدامـي ⌨:**

-هالاوامــر الـمـتـوفـرة . 
/about - مـعـلومـات عـن الـبـوت
/help - هـذه الـرسـاله
/start - تـشـغـيل الـبـوت 
/generate - لـبـدأ اسًتـخـࢪاج جـلـسه جـديـده
/cancel - الـغـاء الـعـمليـة
/restart - للاعـاده
"""

    # About Message
    ABOUT = """
**- حـول هـذا الـبـوت . 

- بـوت يـساعـدك عـلى اسًتـخـࢪاج كـود تـيـرمـكـس  .

- الـدعـم للـمـساعـده : @a_t_9**
    """
