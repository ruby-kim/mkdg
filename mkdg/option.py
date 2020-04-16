"""
Implement parameter options
"""
import argparse
from argparse import RawTextHelpFormatter


def setting_parse():
    """
        Setting input format

        Returns:
            :param: filename(array): the name array of files
    """
    parser = argparse.ArgumentParser(description='옵션을 선택해주세요.', formatter_class=RawTextHelpFormatter)
    parser.add_argument('--filename', required=True, nargs='+', help='맞춤법이 틀린 데이터를 생성할 txt 파일명을 입력해주세요: 파일명.txt\n'
                                                          '한 개 이상 입력해주세요.\n'
                                                          ' ex) text1.txt text2.txt text3.txt\n\n')

    args = parser.parse_args()
    filenames = args.filename
    return filenames
