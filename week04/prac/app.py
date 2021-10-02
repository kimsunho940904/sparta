from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('index.html')


## API 역할을 하는 부분
# GET방식으로 요청하면 /test url이 실행된다.
# GET방식에 파라미터로 전달 방법?? http://localhost:5000/test?title_give=hello , ? 이후에 title_give = key가 되고, hello는 value가 된다.
@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


@app.route('/test', methods=['POST'])
def test_post():
    # title_receive = request.form['title_give']
    title_receive = request.form.get('title_give')
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
