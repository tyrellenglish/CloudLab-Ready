import geni.portal as portal
import geni.rspec.pg as pg

pc = portal.Context()
rspec = pg.Request()


node = rspec.RawPC("node")


node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD"


node.addService(pg.Execute(
    shell="bash",
    command="bash /local/repository/scripts/cloudlab/bootstrap.sh"
))

pc.printRequestRSpec(rspec)

