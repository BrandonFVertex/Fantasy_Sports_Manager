# ================================
# test.py
# ================================
# Do not modify the test file unless directed by your teacher.

from module import Team
import sys
from os import system


def run_all_tests():
    system("clear")
    print("Running tests...")
    failure = False

    if not test_add_player():
        failure = True

    if not test_total_points():
        failure = True

    if not test_highest_scorer():
        failure = True

    if not test_bench_player():
        failure = True

    if not test_average_points():
        failure = True

    if not test_top_two():
        failure = True

    print("\n==============================")

    if failure:
        print("❌ Some tests failed.")
    else:
        print("✅ All tests passed!")


# ---------------------------------
def test_add_player():

    print("\n--- test_add_player ---")

    failure = False

    tests = [
        ("Mahomes", 25),
        ("Allen", 30),
    ]

    for i, (name, points) in enumerate(tests):

        try:

            team = Team()

            team.add_player(name, points)

            result = team.players[name]

            print(f"Expected: {points}, Got: {result}")

            assert result == points, \
                f"Expected {points}, got {result}"

            print(f"Test {i}: Pass!\n")

        except AssertionError as e:

            print(f"Test {i}: Fail → {e}\n")

            failure = True

        except Exception as e:

            print(
                f"Test {i}: Error → "
                f"{type(e).__name__}: {e}\n"
            )

            failure = True

    return not failure


# ---------------------------------
def test_total_points():

    print("\n--- test_total_points ---")

    failure = False

    try:

        team = Team()

        team.add_player("A", 10)
        team.add_player("B", 5)

        result = team.total_points()

        print(f"Expected: 15, Got: {result}")

        assert result == 15, \
            f"Expected 15, got {result}"

        print("Test 0: Pass!\n")

    except AssertionError as e:

        print(f"Test 0: Fail → {e}\n")

        failure = True

    except Exception as e:

        print(
            f"Test 0: Error → "
            f"{type(e).__name__}: {e}\n"
        )

        failure = True

    return not failure


# ---------------------------------
def test_highest_scorer():

    print("\n--- test_highest_scorer ---")

    failure = False

    try:

        team = Team()

        team.add_player("A", 10)
        team.add_player("B", 30)
        team.add_player("C", 20)

        result = team.highest_scorer()

        print(f"Expected: B, Got: {result}")

        assert result == "B", \
            f"Expected B, got {result}"

        print("Test 0: Pass!\n")

    except AssertionError as e:

        print(f"Test 0: Fail → {e}\n")

        failure = True

    except Exception as e:

        print(
            f"Test 0: Error → "
            f"{type(e).__name__}: {e}\n"
        )

        failure = True

    return not failure


# ---------------------------------
def test_bench_player():

    print("\n--- test_bench_player ---")

    failure = False

    try:

        team = Team()

        team.add_player("Mahomes", 25)

        team.bench_player("Mahomes")

        print("Checking if player was removed...")

        assert "Mahomes" not in team.players, \
            "Player still exists in dictionary"

        print("Test 0: Pass!\n")

    except AssertionError as e:

        print(f"Test 0: Fail → {e}\n")

        failure = True

    except Exception as e:

        print(
            f"Test 0: Error → "
            f"{type(e).__name__}: {e}\n"
        )

        failure = True

    return not failure


# ---------------------------------
def test_average_points():

    print("\n--- test_average_points ---")

    failure = False

    try:

        team = Team()

        team.add_player("A", 10)
        team.add_player("B", 20)

        result = team.get_average_points()

        print(f"Expected: 15, Got: {result}")

        assert result == 15, \
            f"Expected 15, got {result}"

        print("Test 0: Pass!\n")

    except AssertionError as e:

        print(f"Test 0: Fail → {e}\n")

        failure = True

    except Exception as e:

        print(
            f"Test 0: Error → "
            f"{type(e).__name__}: {e}\n"
        )

        failure = True

    return not failure


# ---------------------------------
def test_top_two():

    print("\n--- test_top_two ---")

    failure = False

    try:

        team = Team()

        team.add_player("A", 10)
        team.add_player("B", 30)
        team.add_player("C", 20)

        result = team.get_top_two()

        expected = ["B", "C"]

        print(f"Expected: {expected}, Got: {result}")

        assert result == expected, \
            f"Expected {expected}, got {result}"

        print("Test 0: Pass!\n")

    except AssertionError as e:

        print(f"Test 0: Fail → {e}\n")

        failure = True

    except Exception as e:

        print(
            f"Test 0: Error → "
            f"{type(e).__name__}: {e}\n"
        )

        failure = True

    return not failure


if __name__ == "__main__":

    run_all_tests()

    sys.exit(0)