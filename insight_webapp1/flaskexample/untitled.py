  outputwli = []
        for n in search_results:
           h = 'http://archive.stsci.edu/proposal_search.php?mission=hst&id=' + n
           outputwli.append((n,h))


        links =[]
        for n in results['ds_id']:
            h = 'http://archive.stsci.edu/proposal_search.php?mission=hst&id=' + n
            links.append(h)
        results['url'] = links