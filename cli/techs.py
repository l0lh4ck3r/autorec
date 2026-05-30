def show_technologies(
    repository
):

    technologies = (
        repository.get_technologies()
    )

    for tech in technologies:

        print(
            tech["technology"]
        )