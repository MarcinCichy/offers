def material_costs(i,dimension_x,dimension_y,material_price,material_weight, thicknes, cut_time  ):
    if thicknes <= 5:
        dx = dy = 2*5
    elif thicknes >5 and thicknes <=10:
        dx = dy = 2*10
    else:
        dx = dy = 2*thicknes
    
    dimX_brutto = float(dimension_x+dx)/1000
    dimY_brutto = float(dimension_y+dy)/1000
    detail_material_price = round(((dimX_brutto * dimY_brutto )*material_weight*thicknes*material_price),2)
    return detail_material_price

def cut_price(i,cut_hour_price,cut_time):
    detail_cut_price = round(((cut_hour_price * 60)/3600 * float(cut_time)),2)
    return detail_cut_price
    
def suma_per_detail(i, mat_cost, mat_cut_cost):
    suma_per_detail = mat_cost + mat_cut_cost
    return suma_per_detail
#def all_detail_costs(i,quant_details_cost):
