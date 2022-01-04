from django.shortcuts import render

# Create your views here.
nav_header = ''' <a href="/">Home</a>
        <a href="about">About</a>
        <a href="contact">Contact</a>
        <a href="drug-finder">Drug Finder</a>'''
search_header = ''' <div class="flex">
        <input id='drug-name'type="text" autofocus placeholder="search example: cat fast sachet"></input>
    </div>'''

def home(request):
    return render(request, 'im.html')
    # if request.method == 'POST':
    #     mail = request.form.get('email')
    #     phone_no = request.form.get('phone')
    #     if mail and phone_no:
    #         try:
    #             new_subscriber = Subscriber(mail, phone_no)
    #         except ValueError as error:
    #             return render_template('im.html', page='Home', message=error, form='open-form', side='close-side', category='error' ,header=nav_header)
    #         r = SubsDAO.insert_subs(new_subscriber)
    #         if r == 'success':
    #             r='Success: Your request sent successfuly'
    #             mailprocess = HanldeMailProccess("im-software.net", 25)
    #             mailprocess.send_mail_proccess(mail, "support",
    #             "thesuper_NOVA20", "support@im-software.net", "ahmedsom3a40@hotmail.com")
    #             return render_template('im.html', page='Home', message=r, category='success',header=nav_header)
    #         else:
    #             if r.errno == 1062:
    #                 r = "Phone Number already used"
    #             else:
    #                 r = r.errno
    #             return render_template('im.html', page='Home', message=f'Error: {r}', form='open-form', side='close-side', category='error',header=nav_header)

# def about():
#     return render_template('about.html', page='About',header=nav_header)

# def contact():
#     return render_template('contact.html', page='Contact',header=nav_header)

# def durg():
#     search_options = ['Name','Generic', 'Company', 'Price']
#     return render_template('drugs.html', page='Drug Finder', options=search_options, header=search_header)

# def search():
#     option = request.args.get('option')
#     name = request.args.get('dname')
#     if option and name:
#         new_name = name.replace(' ','%')
#         new_names = list(edits1(new_name))
#         new_search = '|'.join(new_names)
#         if option:
#             drugs = DrugOp.check_input_type(option, name, new_name, new_search)
#             return jsonify(drugs)
    
# def search_alter():
#     alter = request.args.get('gname')
#     drugs = DrugDAO.get_drugs_by_alter(alter)
#     return jsonify(drugs)

# def get_update():
#     pc_name = request.form.get("pc")
#     app_v = float(str(request.form.get("app_v")))
#     for key, values in get_customers().items():
#         if key == pc_name:
#             new_v = values.get("new_v")
#             if isinstance(app_v, float) and isinstance(new_v, float):
#                 if new_v > app_v:
#                     return send_file("./static/files/im.exe", as_attachment=True)
#                 else:
#                     resp = make_response("Up to date", 401)
#                     resp.mimetype = "text/plain"
#                     return resp
#     resp = make_response("not authorized", 401)
#     resp.mimetype = "text/plain"
#     return resp

