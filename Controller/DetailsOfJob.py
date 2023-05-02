from Models.DetailsOfJob import Details as connect
class DetailsOfJobController:
    
    def run(slug):
        result = connect.getDetails("""select `title`,`resume`, `type`, `state`, `city`, `slug`, `link`,`date` from jobs where slug = %s 
        union all 
        select `title`,`resume`, `type`, `state`, `city`, `slug`, `link`,`date` from jobs as job where job.slug <> slug and job.title like title 
        and job.slug is not null 
        or job.slug <> %s limit 0,4""", slug)
        return result