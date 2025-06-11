# class Command:
#     def __init__(self, raw_text: str, is_executed = False):
#         self.raw_text = raw_text
#         self.is_executed = is_executed

#     def mark_as_executed(self):
#         self.is_executed = True
#         return self.is_executed
    
#     def __repr__(self):
#         return f"Command(raw_text='{self.raw_text}',is_excecuted = '{self.is_executed}' )"
    


# ที่อยู่ไฟล์: time_assistant/core/command.py (ฉบับปรับปรุง)

class Command:
    """
    นี่คือ 'พิมพ์เขียว' สำหรับคำสั่งแต่ละคำสั่งที่ผู้ใช้ป้อนเข้ามา
    """

    def __init__(self, raw_text: str):
        self.raw_text = raw_text
        self.is_executed = False # บังคับค่าเริ่มต้น

    def mark_as_executed(self):
        """เปลี่ยนแปลงสถานะของคำสั่งให้เป็น executed"""
        self.is_executed = True # ไม่ต้อง return

    def __repr__(self):
        """แสดงผล Object ให้อ่านง่ายสำหรับนักพัฒนา"""
        # แก้ไข typo และเอา '' ออก
        return f"Command(raw_text='{self.raw_text}', is_executed={self.is_executed})"
    