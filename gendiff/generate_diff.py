"""Function comparing 2 dicts and returning tree with diffs."""


def build_node(name, state, actual_value, previous_value=None):
    """Build node in diff tree."""  # noqa: DAR
    return {
        'name': name,
        'state': state,
        'previous_value': previous_value,
        'actual_value': actual_value,
    }


def generate_diff(dict_before, dict_after):  # noqa: WPS210
    """Take 2 dicts, compare them and build a tree with diff.

    Args:
        dict_before: dict with data before changing (first file)
        dict_after: dict with data after changing (second file)

    Returns:
        tree with diffs
    """
    added_keys = set(dict_after.keys()) - set(dict_before.keys())
    deleted_keys = set(dict_before.keys()) - set(dict_after.keys())
    unite_keys = set(dict_before.keys()) | set(dict_after.keys())

    tree_diff = []

    for added in added_keys:
        tree_diff.append(build_node(
            added,
            'added',
            dict_after[added],
        ))

    for deleted in deleted_keys:
        tree_diff.append(build_node(
            deleted,
            'deleted',
            dict_before[deleted],
        ))

    for key in unite_keys - (added_keys | deleted_keys):
        if dict_before[key] == dict_after[key]:
            tree_diff.append(build_node(
                key,
                'unchanged',
                dict_after[key],
            ))
        else:
            tree_diff.append(build_node(
                key,
                'changed',
                dict_after[key],
                dict_before[key],
            ))

    return tree_diff
