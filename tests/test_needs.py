from awsuse.cli import CFG_KEY_MFA_SERIAL, CFG_KEY_SSO_SESSION, needs_mfa, needs_sso


def test_should_need_mfa():
    assert (
        needs_mfa(
            [
                (CFG_KEY_MFA_SERIAL, ""),
                ("aaaa", "1111"),
                ("bbbb", "2222"),
            ]
        )
        is True
    )


def test_should_not_need_mfa():
    assert (
        needs_mfa(
            [
                ("aaaa", "1111"),
                ("bbbb", "2222"),
            ]
        )
        is False
    )


def test_should_need_sso():
    assert (
        needs_sso(
            [
                (CFG_KEY_SSO_SESSION, ""),
                ("aaaa", "1111"),
                ("bbbb", "2222"),
            ]
        )
        is True
    )


def test_should_not_need_sso():
    assert (
        needs_sso(
            [
                ("aaaa", "1111"),
                ("bbbb", "2222"),
            ]
        )
        is False
    )
