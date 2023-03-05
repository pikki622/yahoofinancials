def remove_prefix(s, prefix):
    return s[len(prefix):] if s.startswith(prefix) else s


def get_request_config(tech_type, req_map):
    return req_map['fundamentals'] if tech_type == '' else req_map['quoteSummary']


def get_request_category(tech_type, fin_types, statement_type):
    return fin_types.get(statement_type, [])[0] if tech_type == '' else tech_type
