from flask import Flask, render_template, request

app = Flask(__name__)

def first_digit(num):
        return int(str(num)[0])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def hello():
    length = float(request.form.get("length[]"))
    width = float(request.form.get("width[]"))
    height = float(request.form.get("height[]"))
    pallets = float(request.form.get("pallets[]"))
    volume = round(length * width * height * pallets,4)
    kilos = float(request.form.get("kilos[]"))
    incoterms = request.form.get("incoterms")
    imo = float(request.form.get("unnum"))

    postcode = request.form.get("postcode")
    
    if postcode == "":
        pass
    else:
        postcode = first_digit(postcode)


    
    field_name_list = request.form.getlist('length[]')
    field_list = []
    for field in field_name_list:
        field_list.append(float(field))
    field_query = sum(field_list)

    width_num_list = request.form.getlist('width[]')
    width_list = []
    for field in width_num_list:
        width_list.append(float(field))
    width_query = sum(width_list)

    height_num_list = request.form.getlist('height[]')
    height_list = []
    for field in height_num_list:
        height_list.append(float(field))
    height_query = sum(height_list)

    pallets_num_list = request.form.getlist('pallets[]')
    pallets_list = []
    for field in pallets_num_list:
        pallets_list.append(float(field))
    pallets_query = sum(pallets_list)

    kilos_num_list = request.form.getlist('kilos[]')
    kilos_list = []
    for field in kilos_num_list:
        kilos_list.append(float(field))
    kilos_query = sum(kilos_list)

    vol_list = [l * w * h * n for l, w, h, n in zip(field_list, width_list, height_list, pallets_list)]

    total_vol = round(sum(vol_list),3)
    total_kgs = round(sum(kilos_list),3)

    if total_vol >= total_kgs/333:
        total_vol = total_vol
    else:
        total_vol = total_kgs/333
    ratio = round(total_kgs/333, 4)

    if incoterms=="exwr":
        zone_A = [2, 3, 4]
        zone_B = [1, 5, 0, 6]
        zone_C = [7]
        zone_D = [8]
        zone_E = [9]
        if postcode in zone_A and total_vol <1.55:
            cost = 80
        elif postcode in zone_B and total_vol <1.55:
            cost = 115
        elif postcode in zone_C and total_vol <1.55:
            cost = 155
        elif postcode in zone_D and total_vol <1.55:
            cost = 143
        elif postcode in zone_E and total_vol <1.55:
            cost = 178
        elif postcode in zone_A and total_vol <97/28:
            cost = 97
        elif postcode in zone_B and total_vol <126/35:
            cost = 126
        elif postcode in zone_C and total_vol <201/63:
            cost = 201
        elif postcode in zone_D and total_vol <189/58:
            cost = 189
        elif postcode in zone_E and total_vol <224/72:
            cost = 224
        elif postcode in zone_A and total_vol <6.05:
            cost = 28 * total_vol
        elif postcode in zone_B and total_vol <6.05:
            cost = 35 * total_vol
        elif postcode in zone_C and total_vol <6.05:
            cost = 63 * total_vol
        elif postcode in zone_D and total_vol <6.05:
            cost = 58 * total_vol
        elif postcode in zone_E and total_vol <6.05:
            cost = 72 * total_vol
        elif postcode in zone_A and total_vol <10.05:
            cost = 26 * total_vol
        elif postcode in zone_B and total_vol <10.05:
            cost = 33 * total_vol
        elif postcode in zone_C and total_vol <10.05:
            cost = 59 * total_vol
        elif postcode in zone_D and total_vol <10.05:
            cost = 56 * total_vol
        elif postcode in zone_E and total_vol <10.05:
            cost = 66 * total_vol
        elif postcode in zone_A and total_vol <15.05:
            cost = 23 * total_vol
        elif postcode in zone_B and total_vol <15.05:
            cost = 31 * total_vol
        elif postcode in zone_C and total_vol <15.05:
            cost = 57 * total_vol
        elif postcode in zone_D and total_vol <15.05:
            cost = 54 * total_vol
        elif postcode in zone_E and total_vol <15.05:
            cost = 63 * total_vol
        elif postcode in zone_A and total_vol >15.05:
            cost = 20 * total_vol
        elif postcode in zone_B and total_vol >15.05:
            cost = 26 * total_vol
        elif postcode in zone_C and total_vol >15.05:
            cost = 54 * total_vol
        elif postcode in zone_D and total_vol >15.05:
            cost = 49 * total_vol
        elif postcode in zone_E and total_vol >15.05:
            cost = 60 * total_vol
    elif incoterms == "exws":
        zone_A = [2, 3, 4]
        zone_B = [1, 5, 0, 6]
        zone_C = [7, 8]
        if postcode in zone_A and total_vol <1.55:
            cost = 57
        elif postcode in zone_B and total_vol <1.55:
            cost = 80
        elif postcode in zone_C and total_vol <1.55:
            cost = 150
    
        elif postcode in zone_A and total_vol <69/24:
            cost = 69
        elif postcode in zone_B and total_vol <90/32:
            cost = 90
        elif postcode in zone_C and total_vol <185/57:
            cost = 185
    
        elif postcode in zone_A and total_vol <6.05:
            cost = 24 * total_vol
        elif postcode in zone_B and total_vol <6.05:
            cost = 32 * total_vol
        elif postcode in zone_C and total_vol <6.05:
            cost = 57 * total_vol
    
        elif postcode in zone_A and total_vol <10.05:
            cost = 21 * total_vol
        elif postcode in zone_B and total_vol <10.05:
            cost = 30 * total_vol
        elif postcode in zone_C and total_vol <10.05:
            cost = 55 * total_vol
    
        elif postcode in zone_A and total_vol <15.05:
            cost = 18 * total_vol
        elif postcode in zone_B and total_vol <15.05:
            cost = 28 * total_vol
        elif postcode in zone_C and total_vol <15.05:
            cost = 54 * total_vol
    
        elif postcode in zone_A and total_vol >15.05:
            cost = 16 * total_vol
        elif postcode in zone_B and total_vol >15.05:
            cost = 24 * total_vol
        elif postcode in zone_C and total_vol >15.05:
            cost = 50 * total_vol

    elif incoterms == "fca":
        if total_vol <1.55:
            cost = 59
    
        elif total_vol <59/14:
            cost = 59
    
        elif total_vol <6.05:
            cost = 14 * total_vol
    
        elif total_vol <10.05:
            cost = 13 * total_vol
    
        elif total_vol <15.05:
            cost = 11 * total_vol
    
        elif total_vol >15.05:
            cost = 10 * total_vol

    if imo == 1:
        imo_c = 195 + 0.2*cost
    elif imo == 2:
        imo_c = 195 + 95 + 0.2*cost
    elif imo == 3:
        imo_c = 195 + 2*95 + 0.2*cost
    elif imo >= 4:
        imo_c = 195 + 2*95 + (imo-3)*50 + 0.2*cost
    elif imo == "":
        imo_c = 0
    else:
        imo_c = 0

    over_c = 0
    for i in range(len(field_list)):
        if field_list[i]>= 8 or width_list[i]>= 8 or height_list[i]>= 8:
            over_c += 150
        elif field_list[i]>= 4 or width_list[i]>= 4 or height_list[i]>= 4:
            over_c += 75
        else:
            over_c += 0

    imo_c = round(imo_c, 2)
    over_c = round(over_c, 2)
    cost = round(cost, 2)
    vgm = 15
    value = round(cost + vgm + imo_c, 2)
    return render_template("index.html", volume=volume, 
        total_kgs=total_kgs, total_vol=total_vol, ratio=ratio, postcode=postcode, vgm = vgm, 
        cost=cost, value = value, imo=imo, imo_c = imo_c, over_c=over_c, field_query=field_query, width_query = width_query)



if __name__ == '__main__':
    app.run(debug = True) 