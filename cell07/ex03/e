def birth(fidict):
    sf = sorted(fidict.values(), key=lambda x: x['datebirth'])

    for figure in sf:
        print(f"{figure['name']} was  {figure['datebirth']}")

if __name__ == "__main__":
    historical_figures = {
        '1': {'name': 'a g', 'datebirth': '1879-03-14'},
        '2': {'name': 'b h', 'datebirth': '1643-01-04'},
        '3': {'name': 'c j', 'datebirth': '1867-11-07'},
        '4': {'name': 'd f', 'datebirth': '1809-02-12'}
    }
    birth(historical_figures)
