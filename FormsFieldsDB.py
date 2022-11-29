# database of fields coordinates to fill in chosen forms
db = {'detain': {'page0':
                      {'name': [0, 0],
                       'surname': [10, 10]},
                 'page1':
                      {'p_end_h': [20, 20],
                       'p_end_date': [30, 40]}
                 },
      'warrant': {'page0':
                      {'name': [1, 1],
                       'surname': [2, 2]}}
      }


def num_pages(form_name):
    return len(db[form_name].keys())


# generator with form positions
def get_form_positions(form_name):
    # iteration trough pages in form
    for i in range(num_pages(form_name)):
        # iteration trough items in pages form
        for k, v in db[form_name][f'page{i}'].items():
            yield k, v


# iteration trough positions in form
cos = iter(get_form_positions('detain'))
try:
    print(list(next(cos)))
    print(next(cos))
    print(next(cos))
    print(next(cos))
    print(next(cos))
    print(next(cos))
    print(next(cos))

except StopIteration:
    print('Done')



# print(db['detain']['page1'].keys())
# string = lambda i: f"page{i}"
# for i in range(2):
#     print(string(i+1))