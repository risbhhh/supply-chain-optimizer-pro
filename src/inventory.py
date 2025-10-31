import numpy as np
import scipy.stats as stats

def inventory_recommendation(mean_demand, std_demand, lead_time, service_level=0.95):
    z = stats.norm.ppf(service_level)
    safety_stock = z * std_demand * (lead_time ** 0.5)
    reorder_point = mean_demand * lead_time + safety_stock
    return dict(safety_stock=int(safety_stock), reorder_point=int(reorder_point))
