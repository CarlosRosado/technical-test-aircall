from src.pagerservice.adapters.abs.PersistencePagerAdapterAbs import PersistencePagerAdapterAbs


class PersistencePagerAdapter(PersistencePagerAdapterAbs):
    """
    Class to manage the information from the Pager store system.
    """

    def get_monitored_service_by_id(self, service_id):
        """
        Get info for the monitored service
        :param service_id: service id
        :return monitored service
        """
        return None

    def save_monitored_service(self, monitored_service):
        """
        Save the monitored service
        :param monitored_service: monitored service to save
        """
        print("Monitored Service saved")
