def material_costs(i,dimensions,material_price,material_weight, thicknes, cut_time  ):
    x_index = dimensions.index('x')
    dimension_x = float(dimensions[0:x_index-1])
    dimension_y = float(dimensions[x_index+2:-3])
    dimX_brutto = float(dimension_x+10)/1000
    dimY_brutto = float(dimension_y+10)/1000
    detail_material_price = round(((dimX_brutto * dimY_brutto )*material_weight*thicknes*material_price),2)
    return detail_material_price

def cut_price(i,cut_hour_price,cut_time):
    detail_cut_price = round(((cut_hour_price * 60)/3600 * float(cut_time)),2)
    return detail_cut_price
    
def suma_per_detail(i, mat_cost, mat_cut_cost):
    suma_per_detail = mat_cost + mat_cut_cost
    return suma_per_detail
#def all_detail_costs(i,quant_details_cost):
