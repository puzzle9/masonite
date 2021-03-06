"""Time Module."""

import pendulum


def cookie_expire_time(str_time):
    """Take a string like 1 month or 5 minutes and returns a pendulum instance.

    Arguments:
        str_time {string} -- Could be values like 1 second or 3 minutes

    Returns:
        pendulum -- Returns Pendulum instance
    """
    if str_time != "expired":
        number = int(str_time.split(" ")[0])
        length = str_time.split(" ")[1]

        if length in ("second", "seconds"):
            # Sat, 06 Jun 2020 15:36:16 GMT
            return (
                pendulum.now()
                .add(seconds=number)
                .format("ddd, DD MMM YYYY H:mm:ss")
            )
        elif length in ("minute", "minutes"):
            return (
                pendulum.now()
                .add(minutes=number)
                .format("ddd, DD MMM YYYY H:mm:ss")
            )
        elif length in ("hour", "hours"):
            return (
                pendulum.now().add(hours=number).format("ddd, DD MMM YYYY H:mm:ss")
            )
        elif length in ("days", "days"):
            return (
                pendulum.now().add(days=number).format("ddd, DD MMM YYYY H:mm:ss")
            )
        elif length in ("week", "weeks"):
            return pendulum.now().add(weeks=1).format("ddd, DD MMM YYYY H:mm:ss")
        elif length in ("month", "months"):
            return (
                pendulum.now()
                .add(months=number)
                .format("ddd, DD MMM YYYY H:mm:ss")
            )
        elif length in ("year", "years"):
            return (
                pendulum.now().add(years=number).format("ddd, DD MMM YYYY H:mm:ss")
            )

        return None
    else:
        return pendulum.now().subtract(years=20).format("ddd, DD MMM YYYY H:mm:ss")


def parse_human_time(str_time):
    """Take a string like 1 month or 5 minutes and returns a pendulum instance.

    Arguments:
        str_time {string} -- Could be values like 1 second or 3 minutes

    Returns:
        pendulum -- Returns Pendulum instance
    """
    if str_time != "expired":
        number = int(str_time.split(" ")[0])
        length = str_time.split(" ")[1]

        if length in ("second", "seconds"):
            return pendulum.now().add(seconds=number)
        elif length in ("minute", "minutes"):
            return pendulum.now().add(minutes=number)
        elif length in ("hour", "hours"):
            return pendulum.now().add(hours=number)
        elif length in ("days", "days"):
            return pendulum.now().add(days=number)
        elif length in ("week", "weeks"):
            return pendulum.now().add(weeks=1)
        elif length in ("month", "months"):
            return pendulum.now().add(months=number)
        elif length in ("year", "years"):
            return pendulum.now().add(years=number)

        return None
    else:
        return pendulum.now().subtract(years=20)
