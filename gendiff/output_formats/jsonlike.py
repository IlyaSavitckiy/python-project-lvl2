"""Function comparing 2 files and making diff in a plate JSON-like format."""

STATES = {  # noqa: WPS407
    'added': ' + ',
    'deleted': ' - ',
    'unchanged': '   ',
}


def generate_output(tree_diff):
    """Take tree diff and transform it to output.

    Args:
        tree_diff: tree (list) with diffs

    Returns:
        diff in json-like format
    """
    output_diff = []
    for diff in tree_diff:
        if diff['previous_value']:
            output_diff.append(
                '{0}{1}: {2}\n{3}{4}: {5}\n'.format(
                    STATES['deleted'],
                    diff['name'],
                    diff['previous_value'],
                    STATES['added'],
                    diff['name'],
                    diff['actual_value'],
                ),
            )
        else:
            output_diff.append(
                '{0}{1}: {2}\n'.format(
                    STATES[diff['state']],
                    diff['name'],
                    diff['actual_value'],
                ),
            )
    return ''.join(['{\n'] + output_diff + ['}'])
