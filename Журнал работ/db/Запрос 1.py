def main():
    db_name = input()
    global_init(db_name)
    session = create_session()
    queryset = session.query(User).filter(User.address == 'module_1', User.speciality.notlike(
        '%engineer%'), User.position.notlike('%engineer%'))
    for colonist in queryset:
        print(colonist.id)


if __name__ == '__main__':
    main()
