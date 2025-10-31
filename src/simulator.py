def simulate_policy(initial_inv, demand_series, reorder_point, order_qty, lead_time):
    inv = initial_inv
    pipeline = []
    stockouts = 0
    holding = 0
    for t, d in enumerate(demand_series):
        arrivals = sum(q for (arr, q) in pipeline if arr == t)
        pipeline = [(arr, q) for (arr, q) in pipeline if arr > t]
        inv += arrivals
        if d > inv:
            stockouts += (d - inv)
            inv = 0
        else:
            inv -= d
        holding += inv
        if inv <= reorder_point:
            pipeline.append((t + lead_time, order_qty))
    return {'stockouts': stockouts, 'avg_inventory': holding/len(demand_series)}
