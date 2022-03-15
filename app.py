from boggle import Boggle
from flask import Flask, request, render_template, session, jsonify

# from django.conf import settings
# from django.conf.urls.static import static

app = Flask(__name__)
boggle_game = Boggle()
app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"

@app.route("/")
def display_board():
	
	board = boggle_game.make_board()
	session["board"] = board


	return render_template("board.html", board=board)

@app.route("/check-word")
def check_word():
	word = request.args["word"]
	board = session["board"]
	response = boggle_game.check_valid_word(board, word)

	return jsonify({'result': response})

@app.route("/post-score", methods=["POST"])
def post_score():
	score = request.json["score"]
	highscore = session.get("highscore", 0)
	nplays = session.get("nplays", 0)

	session['nplays'] = nplays + 1
	session['highscore'] = max(score, highscore)

	return jsonify(brokeRecord=score > highscore)