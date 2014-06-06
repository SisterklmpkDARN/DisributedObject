import sys
from omniORB import CORBA
import CosNaming, HelloApp

# Initialise the ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Obtain a reference to the root naming context
obj         = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print "Failed to narrow the root naming context"
    sys.exit(1)

# Resolve the name "Hello"
name = [CosNaming.NameComponent("Hello", "")]
try:
    obj = rootContext.resolve(name)

except CosNaming.NamingContext.NotFound, ex:
    print "Name not found"
    sys.exit(1)

# Narrow the object
eo = obj._narrow(HelloApp.Hello)

if eo is None:
    print "Object reference is not an Hello"
    sys.exit(1)

# Invoke the echoString operation
message = "Hello World"
result  = eo.echoString(message)

print "I said '%s'. The object said '%s'." % (message,result)