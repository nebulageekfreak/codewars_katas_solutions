def job_matching(candidate, job):
    return job['max_salary'] >= candidate['min_salary'] * 0.9