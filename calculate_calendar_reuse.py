import calendar
import itertools


MIN_YEAR = 1900
MAX_YEAR = 2100


def get_annotated_years(min_year, max_year):
    for year in range(min_year, max_year + 1):
        yield year, calendar.weekday(year, 1, 1), calendar.isleap(year)


def main():
    years = list(get_annotated_years(MIN_YEAR, MAX_YEAR))

    def get_key(x):
        year, weekday, isleap = x
        return (weekday, isleap)

    years.sort(key=get_key)
    grouped = itertools.groupby(years, key=get_key)

    for key, items in grouped:
        print(
            "{}, {}: {}".format(
                calendar.day_name[key[0]],
                "leap" if key[1] else "not leap",
                " ".join(str(x[0]) for x in items),
            )
        )


if __name__ == "__main__":
    main()
