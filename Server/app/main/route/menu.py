import re
from re import search
from flask import Blueprint
from flask.globals import request
from ..models.CategoryModel import CategoryModel,db
import json

menu = Blueprint('menu',__name__)

@menu.route('/',methods=['GET'])
def home():
    # query for all the categories
    category = db.engine.execute("select * from categories ORDER BY category_sequence ASC")
    category_list = [i.name.title() for i in category]

    # arguments for filtering items according to category and veg option
    category_table = request.args.get('category_table',default=category_list[0], type=str)
    veg_only = request.args.get("veg_only",type=str)
    page = request.args.get("page",type=int,default=0)

    #query to find the total items in the category
    total_no_of_items = db.engine.execute("select count(id) from %s"%(category_table))
    total_no_of_items = [dict(i) for i in total_no_of_items][0]["count(id)"] 

    # query to filter for veg options
    if veg_only == "veg":
        items = db.engine.execute("select * from %s WHERE veg='veg' ORDER by item_sequence  ASC LIMIT %d,10"%(category_table, page*10))
        total_no_of_items = db.engine.execute("select count(id) from %s where veg='veg'"%(category_table))
        total_no_of_items = [dict(i) for i in total_no_of_items][0]["count(id)"] 
    else:
        items = db.engine.execute("select * from %s ORDER by item_sequence ASC LIMIT %d,10"%(category_table, page*10))

    item_list = [dict(i) for i in items]

    return json.dumps({"categories": (category_list), "items":item_list,"items_total":total_no_of_items})

@menu.route('/search',methods=['GET'])
def search():
# api to run search request
    category = db.engine.execute("select * from categories ORDER BY category_sequence ASC")
    category_list = [i.name.title() for i in category]

# arguments for filtering items according to category and veg option 
    category_table = request.args.get('category_table',default=category_list[0], type=str)
    veg_only = request.args.get("veg_only",type=str)
    page = request.args.get("page",type=int,default=0)
    search = request.args.get("search",type=str,default='%')

 #query to find the total items in the category     
    total_no_of_items = db.engine.execute("select count(id) from %s"%(category_table))
    total_no_of_items = [dict(i) for i in total_no_of_items][0]["count(id)"] 

# query to filter for veg options
    if veg_only == "veg":
        items = db.engine.execute("select * from %s WHERE veg='veg' and name like '%s' ORDER by item_sequence  ASC LIMIT %d,10"%(category_table,"%%"+search+"%%", page*10))
        total_no_of_items = db.engine.execute("select count(id) from %s where veg='veg'"%(category_table))
        total_no_of_items = [dict(i) for i in total_no_of_items][0]["count(id)"] 
        item_list = [dict(i) for i in items]
        return json.dumps({"categories": (category_list), "items":item_list,"items_total":total_no_of_items})
    else:
        items = db.engine.execute("select * from %s  where name like '%s' ORDER by item_sequence ASC LIMIT %d,10"%(category_table,"%%"+search+"%%", page*10))
        item_list = [dict(i) for i in items]
        return json.dumps({"categories": (category_list), "items":item_list,"items_total":total_no_of_items})
    


