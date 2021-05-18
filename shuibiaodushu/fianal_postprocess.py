'''
识别结果后处理
'''


def final_postProcess():
    SPECIAL_CHARS = {k: v for k, v in zip('ABCDEFGHIJ', '1234567890')}

    test_dir = 'datasets/data/test_imgs'
    rec_res_dir = 'temp/rec_res'
    rec_res_files = os.listdir(rec_res_dir)

    final_res = dict()
    for file in os.listdir(test_dir):
        res_file = file.replace('.jpg', '.txt')
        if res_file not in rec_res_files:
            final_res[file] = ''
            continue

        with open(os.path.join(rec_res_dir, res_file), 'r') as f:
            rec_res = f.readline().strip()
        final_res[file] = ''.join([t if t not in 'ABCDEFGHIJ' else SPECIAL_CHARS[t] for t in rec_res])

    with open('work/final_res.txt', 'w') as f:
        for key, value in final_res.items():
            f.write(key + '\t' + value + '\n')


# 生成最终的测试结果
final_postProcess()