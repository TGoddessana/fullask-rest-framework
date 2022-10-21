from flask import cli

import click


@click.command()
@click.option('--db_id', type=click.STRING, required=True, help='db id plz')
@click.option('--db_pw', type=click.STRING, required=True, help='db password plz')
@click.option('--log_level', type=click.STRING, required=False, default='INFO')
@click.option('--log_name', type=click.STRING, required=False, default='alpha')
def main(db_id, db_pw, log_level, log_name):
    print(F'DB아이디: {db_id}  DB비밀번호: {db_pw}')
    print(F'로그레벨: {log_level} 로그파일명: {log_name}.log')


if __name__ == '__main__':
    main()