def index_all(my_input: list[any], to_find: any) -> any:
        ret = []
        for index, value in enumerate(my_input):
                if value == to_find:
                        ret.append(index)
                elif isinstance(value, list):
                        inner_ret = []
                        for inner_index, inner_value in enumerate(value):
                                if inner_value == to_find:
                                    inner_ret.append(inner_index)
                        ret.append(inner_ret)
        return ret

print(index_all([3, [1,3,3,6]], 3))