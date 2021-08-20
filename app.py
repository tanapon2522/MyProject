from flask import Flask , request
import json

from BinanceTrade.Trade import ReceiveSignals

app = Flask(__name__)

@app.route("/SIGNALS" , methods=['POST'])
def SIGNALS_RECEIVER():
    if request.method == "POST": # ลืมเครื่องหมาย : ครับ
        msg = request.data.decode("utf-8")
        json_msg = json.loads(msg)
        print(json_msg) # <-- dictionary

        msg = ReceiveSignals(signal_data_dict = json_msg)
               

    # สร้างฟังก์ชั่น ในการจัดการข้อมูล
    #"""
    #{"SYMBOL":"{{ticket}}",
    #"SIGNALS":{{strategy.order.action}}"}
    #"""
    return "200"

if __name__ == "__main__":
    app.run(debug=True,port=8088)