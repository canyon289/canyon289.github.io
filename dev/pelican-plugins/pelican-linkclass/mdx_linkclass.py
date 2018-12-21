"""Markdown extension for the Link Class plugin for Pelican"""

## Copyright (C) 2015, 2017  Rafael Laboissiere
##
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Affero Public License as published by
## the Free Software Foundation, either version 3 of the License, or (at
## your option) any later version.
##
## This program is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## Affero General Public License for more details.
##
## You should have received a copy of the GNU Affero General Public License
## along with this program.  If not, see http://www.gnu.org/licenses/.


from markdown import Extension
from markdown.inlinepatterns import LinkPattern, LINK_RE
from markdown.inlinepatterns import ReferencePattern, REFERENCE_RE
import re
import sys

### Utlity function for adding the appropriate class attribute
def add_class (elm, config):
   m = re.match ('^https?://', elm.get ('href'))
   elm.set ('class',
            m and config ['external-class']
              or config ['internal-class'])
   return elm

class LinkClass (LinkPattern):
    """Markdown inline pattern processor for adding class attribute to
inline-style hyperlinks"""

    def __init__ (self, md, config):
        """Initialize the Markdwon inline pattern processor"""

        ## Store the configuration dict
        self.config = config

        ## Initialize the parent class
        LinkPattern.__init__ (self, LINK_RE, md)

    def handleMatch (self, m):
        """Add the class attribute to the generated <a> element"""

        ## Build the <a> element using the parent class
        elm = LinkPattern.handleMatch (self, m)

        ## Return the <a> element
        return add_class (elm, self.config)

class ReferenceClass (ReferencePattern):
    """Markdown inline pattern processor for adding class attribute to
reference-style hyperlinks"""

    def __init__ (self, md, config):
        """Initialize the Markdwon inline pattern processor"""

        ## Store the configuration dict
        self.config = config

        ## Initialize the parent class
        ReferencePattern.__init__ (self, REFERENCE_RE, md)

    def handleMatch (self, m):
        """Add the class attribute to the generated <a> element"""

        ## Build the <a> element using the parent class
        elm = ReferencePattern.handleMatch (self, m)

        ## Return the <a> element
        return add_class (elm, self.config)

class LinkClassExtension (Extension):
    """Markdown extension for the Link Class plugin"""

    def __init__(self, config):
        """Initialize the Markdown extension"""
        self.config = config

    def extendMarkdown (self, md, md_globals):
        """Register the Markdown extension"""

        ## LinkClass instances is added to the list of inline pattern
        ## processors, just before the processor defined for the "link" and
        ## the "reference" objects, such that the normal behavior is
        ## overridden.
        md.inlinePatterns.add ('linkclass',
                               LinkClass (md, self.config),
                               '<link')
        md.inlinePatterns.add ('referenceclass',
                               ReferenceClass (md, self.config),
                               '<reference')
