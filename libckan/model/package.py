__author__ = 'dgraziotin'

import serializable
import resource
import trackingsummary
import tag

class Package(serializable.Serializable):
    def __init__(self, name=''):
        self.id = ''
        self.name = name
        self.title = ''
        self.type = None
        self.version = None
        self.state = ''
        self.revision_id = ''
        self.revision_timestamp = ''
        self.url = None
        self.ckan_url = ''
        self.download_url = ''
        self.notes_rendered = ''
        self.notes = ''
        self.tracking_summary = trackingsummary.TrackingSummary()

        self.license_id = 'notspecified'
        self.license = ''
        self.license_title = 'License Not Specified'
        self.licese_url = ''

        self.author = ''
        self.author_email = ''
        self.maintainer = ''
        self.maintainer_email = ''
        self.owner_org = None
        self.organization = None

        self.tags = [] #TODO convert to objects
        self.num_tags = 0
        self.groups = [] #TODO convert to objects
        self.isopen = True
        self.private = False
        self.metadata_created = ''
        self.metadata_modified = ''
        self.relationships = [] #TODO convert to objects

        self.resources = []
        self.num_resources = 0

        self.ratings_count = 0
        self.rating_average = 0.0

        self.extras = [] #TODO convert to objects

    def add_resource(self, resource):
        self.resources.append(resource)

    def add_tag(self, tag):
        self.tags.append(tag)
        self.num_tags = len(self.tags)

    #def add_relationship(self, package):
    #    #TODO
    #    pass

    @classmethod
    def from_dict(cls, dict):
        pkg = Package()
        for key in dict.keys():
            if pkg.__dict__.has_key(key):
                if key == 'resources':
                    for resource_dict in dict[key]:
                        pkg.add_resource(resource.Resource.from_dict(resource_dict))
                elif key == 'tracking_summary':
                    pkg.tracking_summary = trackingsummary.TrackingSummary.from_dict(dict[key])
                elif key == 'tags':
                    for tag_dict in dict[key]:
                        pkg.add_tag(tag.Tag.from_dict(tag_dict))
                else:
                    pkg.__dict__[key] = dict[key]
        return pkg