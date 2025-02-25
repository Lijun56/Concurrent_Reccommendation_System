from recall.context import Context
from flask import Flask, request, jsonify
from recall.service import recall_service

app = Flask('recall_service_app')

@app.route('/recall')
def get_anime():
    user.id = request.args.get('user_id', type=int)
    print(f'Calling user {user_id}...')
    context = Context(user_id)
    res = recall_service.anime_recall(context)
    return jsonify(res)
@app. route("/sim" )
def get_sim_anime():
    anime_id = request.args-get( 'anime_id', type=int)
    if anime_id is None:
        return 'bad anime id', 400
    context = Context(None, anime_id)
    res = recall_service.similar_animes(context)
    return jsonify (res)

